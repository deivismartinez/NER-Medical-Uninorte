import subprocess
import argparse

def evaluate(file_type, model_index):
    process = "evaluate.py brat spans"
    gold ="systemd/gold/"
    system = "systemd/model_"+str(model_index)+"/test"+str(file_type)+"/"
    response = subprocess.getoutput(f"{process} {gold} {system}")
    responses = response.split('\n')
    do_file(responses=responses)
    #subprocess.call(process, shell=True)

def do_file(responses):
    list = []
    dict = {}
    for row in responses:
       # print(row)
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
            list.append(dict)
    for line in list:
        print (line)

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
    evaluate(2, 2)
    