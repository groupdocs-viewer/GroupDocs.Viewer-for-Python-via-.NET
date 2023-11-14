# reorder_pages.py
# This example demonstrates how to reorder pages in the output PDF document.

import os
import aspose.groupdocsviewer as gv
import aspose.groupdocsviewer.options as gvo
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    output_file_path = os.path.join(output_directory, "output.pdf")

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with gv.Viewer(test_files.sample_docx) as viewer:
        pdf_options = gvo.PdfViewOptions(output_file_path)

        # Pass page numbers in the order you want to render them
        viewer.view(pdf_options, [2, 1])

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
