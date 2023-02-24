import subprocess
import argparse
import json

def evaluate(file_type, model):
    process = "evaluate.py brat spans"
    gold ="systemd/gold/"
    system = "systemd/model_"+str(model.get("id"))+"/test"+str(file_type)+"/"
    response = subprocess.getoutput(f"{process} {gold} {system}")
    responses = response.split('\n')
    do_file(responses=responses,model = model,file_type = file_type)
    #subprocess.call(process, shell=True)
    
def compare():
    file = open("systemd/models.json","r")
    models = json.load(file).get("models")
    file.close()
    file= open("tabla_modelos.txt","w")
    global file_t
    file_t= open("tabla_results.txt","w")
    file_t.write("ID\tModel\tPrecision\tRecall\tF1\tTipo\tSub-track\n")
    for model in models:
        file.write(str(model.get("id"))+"\t"+model.get("name")+"\n")
        for i in range(0,4):
            evaluate(file_type = i, model = model)
        #print(model)
    file.close ()
    file_t.close ()
    
def do_file(responses, model, file_type):
    list = [] 
    dict = {}
    for row in responses:
        #print(row)
        if "SubTrack 2 [" in row :
            index_st = row.index("SubTrack 2 [")
            dict["SubTrack 2"]=row[index_st+12:index_st+18]
        if "Measure        " in row :
            index_st = row.index("Measure        ")
            dict["Measure"]=row[index_st+15:len(row)].strip()
        if "Precision      " in row :
            index_st = row.index("Precision      ")
            dict["Precision"]=row[index_st+15:len(row)].strip()
        if "Recall         " in row :
            index_st = row.index("Recall         ")
            dict["Recall"]=row[index_st+15:len(row)].strip()
        if "F1             " in row :
            index_st = row.index("F1             ")
            dict["F1"]=row[index_st+15:index_st+20].strip()
            dict["model"]=model.get("name")
            dict["id"]=model.get("id")
            dict["file_type"]=file_type
            list.append(dict)
            dict = {}    
    for line in list:
        print (line)
        file_t.write(str(line.get("id"))+"\t"+line.get("model")
        +"\t"+str(line.get("Precision"))+"\t"+str(line.get("Recall"))
        +"\t"+str(line.get("F1"))+"\t"+str(line.get("file_type"))+"\t"+str(line.get("SubTrack 2"))+"\n")

if __name__ == "__main__":
    """
    parser = argparse.ArgumentParser(description="Evaluation script for the TESIS track.")
    parser.add_argument("file_type",
                        choices=["0", "1", "2", "3"],
                        help="Type_not_exist")
    parser.add_argument("model_index",
                        choices=["1", "2", "3","4","5","6","7"],
                        help="Model_index_not_exist")
    args = parser.parse_args()
    evaluate(args.file_type, args.model_index)
    """
    compare()
    