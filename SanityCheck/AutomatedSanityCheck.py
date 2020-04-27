# v1.0 - 26.02.2020: - Sanity check all .cpp files
# v1.01 - 27.02.2020: - Added support for batch file processing
# v1.1 - 26.04.2020: - Added support for multiple file endings
# - Added support for changing the number of batches

import os
import time
from datetime import date
import Helper.FilePostHelper as file 

#os.chdir("Cpp-Area")

#file.postToGithubInBatches()

#file.testFileParsing()

file.recursiveScan()