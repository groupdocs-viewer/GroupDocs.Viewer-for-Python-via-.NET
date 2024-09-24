# get_view_info_for_project_document.py
# This example demonstrates how to get view info for MS Project document.

import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import groupdocs.viewer.results as gvr
from groupdocs.pycore import *
import os
import test_files

def run():
    with gv.Viewer(test_files.sample_mpp) as viewer:
        options = gvo.ViewInfoOptions.for_html_view()
        view_info = viewer.get_view_info(options)       
        
        info = cast(gvr.ProjectManagementViewInfo, view_info)        
        print("Document type is: " + str(info.file_type))
        print("Pages count: " + str(len(info.pages)))
        print("Project start date: {0}".format(info.start_date))
        print("Project end date: {0}".format(info.end_date))

    print("\nView info retrieved successfully.")

if __name__ == "__main__":
    run()
