# get_view_info_for_archive_file.py
# This example demonstrates how to get view info for Archive files.

import aspose.groupdocsviewer as gv
import aspose.groupdocsviewer.options as gvo
import aspose.groupdocsviewer.results as gvr
import os
import test_files
from aspose.pycore import *

def run():
    with gv.Viewer(test_files.sample_zip_with_folders) as viewer:
        info = viewer.get_view_info(gvo.ViewInfoOptions.for_html_view())

        print("File type:", info.file_type)
        print("Pages count:", len(info.pages))

        print("Folders:")
        print(" - /")

        root_folder = ""
        read_folders(viewer, root_folder)

    print("\nView info retrieved successfully.")

def read_folders(viewer, folder):
    options = gvo.ViewInfoOptions.for_html_view()
    options.archive_options.folder = folder

    view_info = viewer.get_view_info(options)
    archive_view_info = cast(gvr.ArchiveViewInfo, view_info)
    
    for sub_folder in archive_view_info.folders:
        print(f" - {sub_folder}")
        read_folders(viewer, sub_folder)

if __name__ == "__main__":
    run()
