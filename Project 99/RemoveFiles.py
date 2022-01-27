import os
import shutil
import time

path="C:/Users/gauri/OneDrive/Desktop/Python/CheckForDeletion"
for(root,folder,files) in os.walk(path):
    print(root)
    print(folder)
    print(files)
    hour=time.time()
    newTime=os.stat(path).st_ctime
    #hour-(newTime)>hour
    print(hour)
    print(newTime)
if(newTime>hour):
    shutil.rmtree(path)
    for i in folder():
        folderTime=os.stat(path).st_ctime
    for i in files():
        fileTime=os.stat(path).st_ctime
    

