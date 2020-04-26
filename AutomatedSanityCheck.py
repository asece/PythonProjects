# v1.0 - 26.02.2020:
# - Sanity check all .cpp files
# v1.01 - 27.02.2020;
# - Added support for batch file processing
# v1.1 - 26.04.2020: 
# - Added support for multiple file endings
# - Added support for changing the number of batches

import os
import time
from datetime import date

BATCHES = 6
EXTENSIONS = [".c",",h",".cpp",".hpp",".py",".js",".cs"]

def line_prepender(filename, line, line0):
    with open(filename, 'r+') as f:
        rline = f.readline()
        if(line0 in rline):
            print("Not a new file")
            content = f.read()
            content.splitlines()
            content.splitlines(True)[1:]
            f.seek(0, 0)
            f.write(line.rstrip('\r\n') + '\n' + content)
        else:    
            with open(filename, 'r+') as f:    
                content = f.read()
                f.seek(0, 0)
                f.write(line.rstrip('\r\n') + '\n' + content)

def postToGithubInBatches():
    for x in range(BATCHES):
        i = 0
        for file in os.listdir(os.getcwd()):
            if (i%BATCHES == x):
                if file.endswith(tuple(EXTENSIONS)):
                    print ("Working on",i,file)
                    line_prepender(file, line,line0) 
            i =i+1
        os.system('"git status"')
        os.system('"git add -A"')
        os.system('"git commit -m "Automated Sanity Check"')
        os.system('"git push"')
        time.sleep(5)

today = date.today()
print("Running check for date:", today)
line0 = "//  Last sanity check: "
line = line0 + str(today)

os.chdir("Cpp-Area")

postToGithubInBatches()
