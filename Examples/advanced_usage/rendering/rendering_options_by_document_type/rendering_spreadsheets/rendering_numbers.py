# rendering_numbers.py
# This example demonstrates how to render an Apple Numbers document into HTML, JPG, PNG, PDF.

import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import os
from os.path import join
import test_files
import utils

def run():
    # Update with the path to your output directory
    output_directory = utils.get_output_directory_path()

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    page_file_full_path = join(output_directory, "Numbers_result.html")

    # TO MULTI PAGES HTML
    with gv.Viewer(test_files.sample_numbers) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_full_path)
        viewer.view(options)

    # TO JPG
    page_file_full_path = join(output_directory, "Numbers_result.jpg")
    with gv.Viewer(test_files.sample_numbers) as viewer:
        options = gvo.JpgViewOptions(page_file_full_path)
        viewer.view(options)

    # TO PNG
    page_file_full_path = join(output_directory, "Numbers_result.png")
    with gv.Viewer(test_files.sample_numbers) as viewer:
        options = gvo.PngViewOptions(page_file_full_path)
        viewer.view(options)

    # TO PDF
    page_file_full_path = join(output_directory, "Numbers_result.pdf")
    with gv.Viewer(test_files.sample_numbers) as viewer:
        options = gvo.PdfViewOptions(page_file_full_path)
        viewer.view(options)

    # Indicate the successful rendering of the source document and specify where to find the output in the specified directory
    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}")

if __name__ == "__main__":
    run()
