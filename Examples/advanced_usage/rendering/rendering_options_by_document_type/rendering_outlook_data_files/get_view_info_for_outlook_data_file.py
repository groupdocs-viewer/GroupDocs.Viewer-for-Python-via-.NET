# get_view_info_for_outlook_data_file.py
# This example demonstrates how to get view info for Outlook data file.

import aspose.groupdocsviewer as gv
import aspose.groupdocsviewer.options as gvo
import aspose.groupdocsviewer.results as gvr
from aspose.pycore import *
import os
import test_files

def run():
    with gv.Viewer(test_files.sample_ost_subfolders) as viewer:
        options = gvo.ViewInfoOptions.for_html_view()
        view_info = viewer.get_view_info(options)
        root_folder_info = cast(gvr.OutlookViewInfo, view_info)
                        
        print("File type is: " + str(root_folder_info.file_type))
        print("Pages count: " + str(len(root_folder_info.pages)))

        for folder in root_folder_info.folders:
            print(folder)

    print("\nView info retrieved successfully.")

if __name__ == "__main__":
    run()
