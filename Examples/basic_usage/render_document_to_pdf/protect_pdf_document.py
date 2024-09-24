# protect_pdf_document.py
# This example demonstrates how to protect the output PDF document.

import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import os
from os.path import join
import test_files
import utils
 
def run():
    output_directory = utils.get_output_directory_path()
    output_file_path = join(output_directory, "output.pdf")

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with gv.Viewer(test_files.sample_docx) as viewer:
        security = gvo.Security()
        security.document_open_password = "o123"
        security.permissions_password = "p123"
        security.permissions = gvo.Permissions.ALLOW_ALL & ~gvo.Permissions.DENY_PRINTING

        pdf_options = gvo.PdfViewOptions(output_file_path)
        pdf_options.security = security

        viewer.view(pdf_options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
