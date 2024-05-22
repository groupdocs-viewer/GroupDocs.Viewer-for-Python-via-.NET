# This example demonstrates how to render a document into HTML.

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

    page_file_path_format = join(output_directory, "page_{0}.html")

    with gv.Viewer(test_files.sample_docx) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        viewer.view(options)

    # Indicate the successful rendering of the source document and specify where to find the output in the specified directory
    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")
