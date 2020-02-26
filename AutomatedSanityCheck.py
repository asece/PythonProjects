import os
from datetime import date

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

for file in os.listdir(os.getcwd()):
    if file.endswith(".cpp"):
        print ("Checking",file)
        line_prepender(file, line,line0)

os.system('"git status"')
os.system('"git add -A"')
os.system('"git commit -m "Automated Sanity Check"')
os.system('"git push"')
