import os
saved_path=os.getcwd() #equivalent to pwd in *nix
list1=[] #List of the filenames you want to keep
os.chdir("E:\New folder") #chdir to the directory containg files. 
for filename in os.listdir("."):
    flag=0
    for items in list1:
        if filename.find(str(items))!=-1:
            flag=1
    if flag == 0:
        os.remove(filename)
os.chdir(saved_path) #return back to the original working directory.
