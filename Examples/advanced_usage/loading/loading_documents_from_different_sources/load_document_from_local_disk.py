# load_document_from_local_disk.py
# This example demonstrates how to render tracked changes.

import os
import aspose.groupdocsviewer as gv
import aspose.groupdocsviewer.options as gvo
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = os.path.join(output_directory, "page_{0}.html")

    with gv.Viewer(test_files.sample_docx) as viewer:
        html_options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        viewer.view(html_options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
