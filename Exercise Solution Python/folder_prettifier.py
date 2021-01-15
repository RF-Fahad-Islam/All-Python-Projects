import os
#!Folder Prettifier
def soldier(path, filepath, Format):
    os.chdir(path)
    i = 1
    with open(filepath) as f:
        filelist = f.read().split("\n")
    files = os.listdir(path)
    for File in files:
        if File not in filelist:
            os.rename(File, f"{File.capitalize()}")
            if str(os.path.splitext(File)[1]) == Format:
                # if f"{i}{Format}" not in files:
                os.rename(File, f"{i}{Format}")
                i += 1
soldier(r"C:\Users\user\Desktop\testing",r"C:\Users\user\Documents\Python Codes\fileList.txt", ".txt")