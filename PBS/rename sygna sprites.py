import os
import shutil

directory = "C:\\Users\\jlee4\\Documents\\3.4 GC\\3.4 GC\\Game\\Graphics\\Characters"

for file in os.listdir(directory):
    f = os.path.join(directory,file)
    if "SYGNASUIT" in f:
        print(file[9:])
        target = f"C:\\Users\\jlee4\\Documents\\3.4 GC\\3.4 GC\\Game\\Graphics\\Characters\\SYGNA{file[9:]}"
        shutil.copyfile(f, target)
        os.remove(f)
