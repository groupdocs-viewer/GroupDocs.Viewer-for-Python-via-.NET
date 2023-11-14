# rendering_pst_and_ost.py
# This example demonstrates how to render PST/OST document into HTML, JPG, PNG, PDF.

import aspose.groupdocsviewer as gv
import aspose.groupdocsviewer.options as gvo
import os
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = os.path.join(output_directory, "PST_result.html")
    
    with gv.Viewer(test_files.sample_pst) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        viewer.view(options)
    
    page_file_path_format = os.path.join(output_directory, "PST_result_{0}.jpg")

    with gv.Viewer(test_files.sample_pst) as viewer:
        options = gvo.JpgViewOptions(page_file_path_format)
        viewer.view(options)

    page_file_path_format = os.path.join(output_directory, "PST_result_{0}.png")

    with gv.Viewer(test_files.sample_pst) as viewer:
        options = gvo.PngViewOptions(page_file_path_format)
        viewer.view(options)

    page_file_path_format = os.path.join(output_directory, "PST_result.pdf")

    with gv.Viewer(test_files.sample_pst) as viewer:
        options = gvo.PdfViewOptions(page_file_path_format)
        viewer.view(options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
