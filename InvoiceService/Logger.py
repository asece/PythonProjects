import os
import inspect
from datetime import datetime
dirName = 'Logs'
import threading

def InspectHelper():
    return inspect.stack()[-1].filename

def GetModuleName():
    return InspectHelper()

if not os.path.exists(dirName):
    os.mkdir(dirName)

dateTimeObj = datetime.now()
date = dateTimeObj.strftime("%d.%m.%Y")
logFileName = dirName + "\\" + "Log." + str(os.getpid()) + "." + date + ".log"

LOG_FILE = open(logFileName, "w+")  
LOG_FILE.write("Started log file\n")

def Log(message):
    lock = threading.Lock()
    lock.acquire()
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d:%m:%Y-%H:%M:%S")
    LOG_FILE.write(str(timestampStr) + "::" + message + '\n')
    lock.release()