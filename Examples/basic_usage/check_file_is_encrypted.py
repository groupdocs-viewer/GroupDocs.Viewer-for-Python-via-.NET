# check_file_is_encrypted.py
# This example demonstrates how to check if the file is encrypted.

import groupdocs.viewer as gv
# import groupdocs.viewer.results as gvr
# from groupdocs.pycore import *
import test_files

def run():    
    with gv.Viewer(test_files.encrypted) as viewer:
        file_info = viewer.get_file_info() 
        
        print("File type is: " + str(file_info.file_type))
        print("File encrypted: " + str(file_info.encrypted))

    print("\nFile info retrieved successfully.")
