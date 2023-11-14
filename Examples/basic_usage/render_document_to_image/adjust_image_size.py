# adjust_image_size.py
# This example demonstrates how to adjust the width and height of the output images.

import aspose.groupdocsviewer as gv
import aspose.groupdocsviewer.options as gvo
import os
from os.path import join
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = join(output_directory, "page_{0}.jpg")

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with gv.Viewer(test_files.sample_docx) as viewer:
        jpg_options = gvo.JpgViewOptions(page_file_path_format)
        jpg_options.width = 600
        jpg_options.height = 800

        viewer.view(jpg_options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
