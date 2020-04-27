import os
import time

def insertDateOfCheck(filename, line, line0):
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