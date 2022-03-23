import time
import os
import shutil

keyword = input("Insert keyword")
def main() :
    path = "/Users/shardularya/Desktop/WhiteHatJr./Python-Files"
    print("start")
    filesWithKeyword = []
    foldersWithKeyword = []
    if os.path.exists(path) :
        for rootFolder,folders,files in os.walk(path) : 
                for folder in folders :
                    folder_path = os.path.join(rootFolder,folder)
                    if keyword in folder:
                        foldersWithKeyword.append(folder_path)
                for file in files :
                    file_path = os.path.join(rootFolder,file)
                    if keyword in file:
                        filesWithKeyword.append(file_path)
    else :
        print("File Doesn't Exist")
    newpath = f"{path}/{keyword}"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    for i in foldersWithKeyword :
        print(i)
        print(newpath)
#        try:
#            shutil.rmtree(newpath)
        folderToCopy = os.path.join(newpath, os.path.basename(i))
        print(newpath)
        print(folderToCopy)
        shutil.copytree(i, folderToCopy)
#        except OSError as exc:
#            if exc.errno in (errno.ENOTDIR):
#                shutil.copy(i, newpath)
#            else: print("Directory Not Copied")
    for i in filesWithKeyword :
        shutil.copy2(i, newpath)
main()