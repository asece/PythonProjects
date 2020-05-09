import os
from datetime import datetime
dirName = 'Logs'
import logging

# Basic logging functionality. Accepts only a tring for logging
# TODO Make the logger smarter

if not os.path.exists(dirName):
    os.mkdir(dirName)

dateTimeObj = datetime.now()
date = dateTimeObj.strftime("%d.%m.%Y")
logFileName = dirName + "\\" + "Log." + date + ".log"

LOG_FILE = open(logFileName, "w+")  
LOG_FILE.write("Started log file\n")

def Log(message):
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d:%m:%Y-%H:%M:%S")
    LOG_FILE.write(str(timestampStr) + "::" + message + '\n')