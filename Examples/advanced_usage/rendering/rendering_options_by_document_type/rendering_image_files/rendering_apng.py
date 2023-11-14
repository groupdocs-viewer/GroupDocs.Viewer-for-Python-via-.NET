# rendering_apng.py
# This example demonstrates how to render Animated PNG format

import aspose.groupdocsviewer as gv
import aspose.groupdocsviewer.options as gvo
import os
from os.path import join
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = join(output_directory, "apng_result.html")

    # TO HTML
    with gv.Viewer(test_files.sample_apng) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        viewer.view(options)

    # TO JPG
    page_file_path_format = join(output_directory, "apng_result_{0}.jpg")
    with gv.Viewer(test_files.sample_apng) as viewer:
        options = gvo.JpgViewOptions(page_file_path_format)
        viewer.view(options)

    # TO PNG
    page_file_path_format = join(output_directory, "apng_result_{0}.png")
    with gv.Viewer(test_files.sample_apng) as viewer:
        options = gvo.PngViewOptions(page_file_path_format)
        viewer.view(options)

    # TO PDF
    page_file_path_format = join(output_directory, "apng_result.pdf")
    with gv.Viewer(test_files.sample_apng) as viewer:
        options = gvo.PdfViewOptions(page_file_path_format)
        viewer.view(options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
