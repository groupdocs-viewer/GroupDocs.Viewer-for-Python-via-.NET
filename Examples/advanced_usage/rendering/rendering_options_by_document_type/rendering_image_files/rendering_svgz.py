# rendering_svgz.py
# This example demonstrates how to render SVG/SVGZ document into HTML, JPG, PNG, PDF.

import aspose.groupdocsviewer as gv
import aspose.groupdocsviewer.options as gvo
import os
from os.path import join
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = join(output_directory, "svgz_result.html")

    # TO HTML
    with gv.Viewer(test_files.sample_svgz) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        viewer.view(options)

    # TO JPG
    page_file_path_format = join(output_directory, "svgz_result.jpg")
    with gv.Viewer(test_files.sample_svgz) as viewer:
        options = gvo.JpgViewOptions(page_file_path_format)
        viewer.view(options)

    # TO PNG
    page_file_path_format = join(output_directory, "svgz_result.png")
    with gv.Viewer(test_files.sample_svgz) as viewer:
        options = gvo.PngViewOptions(page_file_path_format)
        viewer.view(options)

    # TO PDF
    page_file_path_format = join(output_directory, "svgz_result.pdf")
    with gv.Viewer(test_files.sample_svgz) as viewer:
        options = gvo.PdfViewOptions(page_file_path_format)
        viewer.view(options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
