# enable_layered_rendering.py
# This example demonstrates how to render a PDF document and place content according to the Z-Index of the content in the source PDF document.

import os
from os.path import join
import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = join(output_directory, "page_{0}.html")

    with gv.Viewer(test_files.sample_pdf) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        options.pdf_options.enable_layered_rendering = True

        viewer.view(options, [1])

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
