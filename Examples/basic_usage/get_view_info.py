# get_view_info.py
# This example demonstrates how to get basic information about document and document view.

import aspose.groupdocsviewer as gv
import aspose.groupdocsviewer.options as gvo
import test_files

def run():
    with gv.Viewer(test_files.sample_pdf) as viewer:
        info = viewer.get_view_info(gvo.ViewInfoOptions.for_html_view())
        print(info)

    print("\nView info retrieved successfully.")
