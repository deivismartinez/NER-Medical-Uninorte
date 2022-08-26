import subprocess
import argparse

def evaluate(file_type, model_index):
    process = "evaluate.py brat spans systemd/gold/ systemd/model_"+model_index+"/test"+file_type+"/"
    subprocess.call(process, shell=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluation script for the TESIS track.")
    parser.add_argument("file_type",
                        choices=["0", "1", "2", "3"],
                        help="Type_not_exist")
    parser.add_argument("model_index",
                        choices=["1", "2", "3","4","5","6","7"],
                        help="Model_index_not_exist")
    args = parser.parse_args()
    evaluate(args.file_type, args.model_index)
    