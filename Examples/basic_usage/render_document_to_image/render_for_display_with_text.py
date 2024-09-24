# This example demonstrates how to render a document so that the extracted text can be placed as a top layer over the image.

import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import os
from os.path import join
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = join(output_directory, "page_{0}.png")

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with gv.Viewer(test_files.sample_docx) as viewer:
        png_options = gvo.PngViewOptions(page_file_path_format)
        png_options.extract_text = True

        viewer.view(png_options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
