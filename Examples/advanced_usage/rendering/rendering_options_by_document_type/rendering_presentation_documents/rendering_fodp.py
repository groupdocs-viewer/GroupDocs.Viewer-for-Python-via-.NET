# rendering_fodp.py
# This example demonstrates how to render FODP document into HTML, JPG, PNG, PDF.

import os
from os.path import join
import aspose.groupdocsviewer as gv
import aspose.groupdocsviewer.options as gvo
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = join(output_directory, "Fodp_result.html")

    with gv.Viewer(test_files.sample_fodp) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        viewer.view(options)

    page_file_path_format = join(output_directory, "Fodp_result.jpg")

    with gv.Viewer(test_files.sample_fodp) as viewer:
        options = gvo.JpgViewOptions(page_file_path_format)
        viewer.view(options)

    page_file_path_format = join(output_directory, "Fodp_result.png")

    with gv.Viewer(test_files.sample_fodp) as viewer:
        options = gvo.PngViewOptions(page_file_path_format)
        viewer.view(options)

    page_file_path_format = join(output_directory, "Fodp_result.pdf")

    with gv.Viewer(test_files.sample_fodp) as viewer:
        options = gvo.PdfViewOptions(page_file_path_format)
        viewer.view(options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
