import pathlib
folder_gold = 'test/'
folder = pathlib.Path(folder_gold)
for file in folder.iterdir():
    #print(file.suffix)
    if file.suffix == ".txt":
        txt_file = open(folder_gold+file.name, "rb")
        text = txt_file.read()
        print(text)
        txt_file.close()
print("Deivis Ángel Martínez Acuña")