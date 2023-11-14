# adjust_quality_when_rendering_to_jpg.py
# This example demonstrates how to adjust the quality of the output JPG images.

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
        jpg_options.quality = 50

        viewer.view(jpg_options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
