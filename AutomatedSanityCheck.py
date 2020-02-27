import os
import time
from datetime import date
CPP_EXT = ".cpp"

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

today = date.today()
print("Running check for date:", today)
line0 = "//  Last sanity check: "
line = line0 + str(today)

os.chdir("Cpp-Area")

i = 0
for file in os.listdir(os.getcwd()):
    if (i%5==0):
        if file.endswith(CPP_EXT):
            print ("Working on",i,file)
            line_prepender(file, line,line0)  
    i = i+1

os.system('"git status"')
os.system('"git add -A"')
os.system('"git commit -m "Automated Sanity Check"')
os.system('"git push"')
time.sleep(5)

i = 0
for file in os.listdir(os.getcwd()):
    if (i%5==1):
            if file.endswith(CPP_EXT):
                print ("Working on",i,file)
                line_prepender(file, line,line0)
    i = i+1
     
os.system('"git status"')
os.system('"git add -A"')
os.system('"git commit -m "Automated Sanity Check"')
os.system('"git push"')
time.sleep(5)
   
i = 0
for file in os.listdir(os.getcwd()):
    if (i%5==2):
            if file.endswith(CPP_EXT):
                print ("Working on",i,file)
                line_prepender(file, line,line0)
    i = i+1
    
os.system('"git status"')
os.system('"git add -A"')
os.system('"git commit -m "Automated Sanity Check"')
os.system('"git push"')
time.sleep(5)
    
i = 0
for file in os.listdir(os.getcwd()):
    if (i%5==3):
            if file.endswith(CPP_EXT):
                print ("Working on",i,file)
                line_prepender(file, line,line0)
    i = i+1
    os.system('"git status"')
    os.system('"git add -A"')
    os.system('"git commit -m "Automated Sanity Check"')
    os.system('"git push"')
    
os.system('"git status"')
os.system('"git add -A"')
os.system('"git commit -m "Automated Sanity Check"')
os.system('"git push"')
time.sleep(5)

i = 0
for file in os.listdir(os.getcwd()):
    if (i%5==4):
            if file.endswith(CPP_EXT):
                print ("Working on",i,file)
                line_prepender(file, line,line0)
    i = i+1

os.system('"git status"')
os.system('"git add -A"')
os.system('"git commit -m "Automated Sanity Check"')
os.system('"git push"')
