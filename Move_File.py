import os
import shutil
source=r"C:\Users\ssjos\Downloads"
destination=r"C:\General Files!\dummy"
list_of_files = os.listdir(source)
print(list_of_files)#
for file in list_of_files:
    name,extension=os.path.splitext(file)
    if extension=="":
        continue
    if extension in [".pdf"]:
        path1=source+"/"+file
        path2=destination+"/"+"pdf_files"
        path3=destination+"/"+"pdf_files"+"/"+file
        if os.path.exists(path2):
            print("movingfiles")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("movingfiles")
            shutil.move(path1,path3)