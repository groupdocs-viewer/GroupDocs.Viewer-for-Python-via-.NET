# rendering_cf2.py
# This example demonstrates how to render CF2 document into HTML, JPG, PNG, PDF.

import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import os
from os.path import join
import test_files
import utils

def render_document(output_directory, input_file, output_format):
    page_file_path_format = join(output_directory, f"cf2_result.{output_format.lower()}")

    with gv.Viewer(input_file) as viewer:
        if output_format == "HTML":
            options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        elif output_format == "JPG":
            options = gvo.JpgViewOptions(page_file_path_format)
        elif output_format == "PNG":
            options = gvo.PngViewOptions(page_file_path_format)
        elif output_format == "PDF":
            options = gvo.PdfViewOptions(page_file_path_format)

        viewer.view(options)

def run():
    output_directory = utils.get_output_directory_path()

    # Render to HTML
    render_document(output_directory, test_files.sample_cf2, "HTML")

    # Render to JPG
    render_document(output_directory, test_files.sample_cf2, "JPG")

    # Render to PNG
    render_document(output_directory, test_files.sample_cf2, "PNG")

    # Render to PDF
    render_document(output_directory, test_files.sample_cf2, "PDF")

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
