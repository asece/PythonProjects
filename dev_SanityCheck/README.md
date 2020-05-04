# Automated sanity file check
  
Tool that automatically looks for compatible files and does something to them.  
Version 1 of the sanity check updates the timestamp of every file it checked.  
The script looks through all of the files from where it starts.  
  
  
If there are more files, they are checked in batches.  
Set program options by modifying the following:  
  
    BATCHES = 6
    MIN_FILES_FOR_BATCH = 5 
    EXTENSIONS = [".c",",h",".cpp",".hpp",".py",".js",".cs"] #
    IGNORE_FILE = "dev_"
    IGNORE_LIST = ["dev_", "__","."]

Feel free to add functionality! :-) 