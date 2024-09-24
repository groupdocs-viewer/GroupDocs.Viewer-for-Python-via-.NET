# rendering_cdr.py
# This example demonstrates how to render CDR document into HTML, JPG, PNG, PDF.

import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import os
from os.path import join
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = join(output_directory, "cdr_result_{0}.html")
    pages = [1]
    # TO HTML
    with gv.Viewer(test_files.sample_cdr) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        viewer.view(options, pages)  # Render the first image

    # TO JPG
    page_file_path_format = join(output_directory, "cdr_result_{0}.jpg")
    with gv.Viewer(test_files.sample_cdr) as viewer:
        options = gvo.JpgViewOptions(page_file_path_format)
        viewer.view(options, pages)  # Render the first image

    # TO PNG
    page_file_path_format = join(output_directory, "cdr_result_{0}.png")
    with gv.Viewer(test_files.sample_cdr) as viewer:
        options = gvo.PngViewOptions(page_file_path_format)
        viewer.view(options, pages)  # Render the first image

    # TO PDF
    page_file_path_format = join(output_directory, "cdr_result.pdf")
    with gv.Viewer(test_files.sample_cdr) as viewer:
        options = gvo.PdfViewOptions(page_file_path_format)
        viewer.view(options, pages)  # Render the first image

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
