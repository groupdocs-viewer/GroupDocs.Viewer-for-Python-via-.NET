# adjust_quality_of_jpg_images.py
# This example demonstrates how to adjust the quality of JPG images in the output PDF document.

import aspose.groupdocsviewer as gv
import aspose.groupdocsviewer.options as gvo
import os
from os.path import join
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    output_file_path = join(output_directory, "output.pdf")

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with gv.Viewer(test_files.jpg_image_pptx) as viewer:
        pdf_options = gvo.PdfViewOptions(output_file_path)
        pdf_options.jpg_quality = 10

        viewer.view(pdf_options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
