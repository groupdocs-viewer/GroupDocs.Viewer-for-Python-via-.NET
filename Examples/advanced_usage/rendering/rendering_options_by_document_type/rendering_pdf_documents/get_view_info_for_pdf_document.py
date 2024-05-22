# get_view_info_for_pdf_document.py
# This example demonstrates how to get view info for a PDF document.

import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import groupdocs.viewer.results as gvr
from groupdocs.pycore import *

import test_files

def run():
    with gv.Viewer(test_files.sample_pdf) as viewer:
        options = gvo.ViewInfoOptions.for_html_view() 
        info = viewer.get_view_info(options)
        pdf_info = cast(gvr.PdfViewInfo, info)

        print("Document type is:", pdf_info.file_type)
        print("Pages count:", len(pdf_info.pages))
        print("Printing allowed:", pdf_info.printing_allowed)

    print("\nView info retrieved successfully.")

if __name__ == "__main__":
    run()
