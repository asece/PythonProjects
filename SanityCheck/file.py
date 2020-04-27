import os
import time
from datetime import date

EXTENSIONS = [".c",",h",".cpp",".hpp",".js",".cs",".py"]
bat = 3
 

def post():
    for x in range(bat):
        print("Posting for ", x)
        i=0
        for file in os.listdir(os.getcwd()):
            if(i%bat == x):
                if (file.endswith(tuple(EXTENSIONS))):
                    print(file)
            i=i+1

post()
