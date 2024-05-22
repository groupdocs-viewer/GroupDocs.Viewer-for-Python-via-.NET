# enable_font_hinting.py
# This example demonstrates how to adjust the display of outline font when rendering PDF documents.

import os
from os.path import join
import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = join(output_directory, "page_{0}.png")

    with gv.Viewer(test_files.hieroglyphs_1_pdf) as viewer:
        options = gvo.PngViewOptions(page_file_path_format)
        options.pdf_options.enable_font_hinting = True

        viewer.view(options, [1])

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
