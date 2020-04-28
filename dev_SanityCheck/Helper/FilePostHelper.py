#  Last sanity check: 2020-04-28
import os
import time
import subprocess
from datetime import date
import Helper.FileEditorHelper as fileEditor

BATCHES = 6
MIN_FILES_FOR_BATCH = 5 
EXTENSIONS = [".c",",h",".cpp",".hpp",".py",".js",".cs"] #
IGNORE_FILE = "dev_"
IGNORE_LIST = ["dev_", "__","."]

today = date.today()
pre_line_C = "//"
pre_line_Py = "#"

print("Running check for date:", today)
line0 = "  Last sanity check: "
line = line0 + str(today)

def postToGithubInBatches():
    for x in range(BATCHES):
        i = 0
        for file in os.listdir(os.getcwd()):
            if (i%BATCHES == x):
                if file.endswith(tuple(EXTENSIONS)):
                    print ("Working on ",i,file)
                    if(".py" in file):
                        line = pre_line_Py + line0 + str(today)
                    else:
                        line = pre_line_C + line0 + str(today)
                    fileEditor.insertDateOfCheck(file, line,line0) 
            i =i+1
        os.system('"git pull"')
        cmd = "git status --porcelain"
        try:
            res = subprocess.check_output(cmd)
            if(len(res) != 0):
                os.system("git status")
                os.system('"git add -A"')
                os.system('"git commit -m "Automated Sanity Check"')
                os.system('"git push"')
                time.sleep(5)
        except:
            print()

def postToGithub():
    for file in os.listdir(os.getcwd()):
            if file.endswith(tuple(EXTENSIONS)):
                print ("Working on ",file)
                if(".py" in file):
                    line = pre_line_Py + line0 + str(today)
                else:
                    line = pre_line_C + line0 + str(today)
                fileEditor.insertDateOfCheck(file, line,line0) 
    os.system('"git pull"')       
    cmd = "git status --porcelain"
    try:
        res = subprocess.check_output(cmd)
        if(len(res) != 0):
            os.system("git status")
            os.system('"git add -A"')
            os.system('"git commit -m "Automated Sanity Check"')
            os.system('"git push"')
            time.sleep(5)
    except:
        print()

def testFileParsing():
    for file in os.listdir(os.getcwd()):
            if file.endswith(tuple(EXTENSIONS)):
                print ("Working on - ",file)
                if(".py" in file):
                    line = pre_line_Py + line0 + str(today)
                    print(line)
                else:
                    line = pre_line_C + line0 + str(today)
                    print(line)

def testFileParsingInBatches():
    for x in range(BATCHES):
        i = 0
        for file in os.listdir(os.getcwd()):
            if (i%BATCHES == x):
                if file.endswith(tuple(EXTENSIONS)):
                    print (i, "Working on - ",file)
                    if(".py" in file):
                        line = pre_line_Py + line0 + str(today)
                        print(line)
                    else:
                        line = pre_line_C + line0 + str(today)
                        print(line)
            i=i+1

def ignoreFile(folder):
    for ignore in IGNORE_LIST:
        if(ignore in folder):
            return True
    

def recursiveScan():
    entries = os.scandir()

    if(len([name for name in os.listdir('.') if os.path.isfile(name)]) > MIN_FILES_FOR_BATCH):
       # Use for testing:
       # testFileParsingInBatches()
       postToGithubInBatches()
    else:
        # Use for testing:
        # testFileParsing()
        postToGithub()

    for entry in entries:
        if(os.path.isdir(entry.name)):
            if(not ignoreFile(entry.name)):
                print("Changing to", entry.name)
                os.chdir(entry.name)
                recursiveScan()
                os.chdir("..")