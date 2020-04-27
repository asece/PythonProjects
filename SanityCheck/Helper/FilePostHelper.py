import os
import time
from datetime import date
import Helper.FileEditorHelper as fileEditor

BATCHES = 6
MIN_FILES_FOR_BATCH = 5 
EXTENSIONS = [".c",",h",".cpp",".hpp"] #,".py",".js",".cs"
IGNORE_FILE = "dev_"

today = date.today()
print("Running check for date:", today)
line0 = "//  Last sanity check: "
line = line0 + str(today)

def postToGithubInBatches():
    for x in range(BATCHES):
        i = 0
        for file in os.listdir(os.getcwd()):
            if (i%BATCHES == x):
                if file.endswith(tuple(EXTENSIONS)):
                    print ("Working on ",i,file)
                    fileEditor.insertDateOfCheck(file, line,line0) 
            i =i+1
        os.system('"git status"')
        os.system('"git add -A"')
        os.system('"git commit -m "Automated Sanity Check"')
        os.system('"git push"')
        time.sleep(5)

def postToGithub():
    for file in os.listdir(os.getcwd()):
            if file.endswith(tuple(EXTENSIONS)):
                print ("Working on ",file)
                fileEditor.insertDateOfCheck(file, line,line0) 
        
    os.system('"git status"')
    os.system('"git add -A"')
    os.system('"git commit -m "Automated Sanity Check"')
    os.system('"git push"')
    time.sleep(5)

def testFileParsing():
    for file in os.listdir(os.getcwd()):
            if file.endswith(tuple(EXTENSIONS)):
                print ("Working on - ",file)

def testFileParsingInBatches():
    for x in range(BATCHES):
        i = 0
        for file in os.listdir(os.getcwd()):
            if (i%BATCHES == x):
                if file.endswith(tuple(EXTENSIONS)):
                    print (i, "Working on - ",file)
            i=i+1

def recursiveScan():
    entries = os.scandir()

    if(len([name for name in os.listdir('.') if os.path.isfile(name)]) > MIN_FILES_FOR_BATCH):
       testFileParsingInBatches()
    else:
        testFileParsing()

    for entry in entries:
        if(os.path.isdir(entry.name) and IGNORE_FILE not in entry.name):
            #print("Changing to", entry.name)
            os.chdir(entry.name)
            recursiveScan()
    os.chdir("..")