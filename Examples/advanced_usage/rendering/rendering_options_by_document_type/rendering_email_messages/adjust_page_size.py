# adjust_page_size.py
# This example demonstrates how to change page size when rendering email messages.

import aspose.groupdocsviewer as gv
import aspose.groupdocsviewer.options as gvo
import os
from os.path import join
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    file_path = join(output_directory, "output.pdf")

    with gv.Viewer(test_files.sample_msg) as viewer:
        options = gvo.PdfViewOptions(file_path)
        options.email_options.page_size = gvo.PageSize.A4

        viewer.view(options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}")

if __name__ == "__main__":
    run()
