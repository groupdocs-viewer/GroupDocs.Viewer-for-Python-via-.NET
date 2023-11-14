# render_selected_pages.py
# This example demonstrates how to render the first and third pages of a document.

import os
import aspose.groupdocsviewer as gv
import aspose.groupdocsviewer.options as gvo
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = os.path.join(output_directory, "page_{0}.html")

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with gv.Viewer(test_files.sample_docx) as viewer:
        html_options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        viewer.view(html_options, [1, 3])

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
