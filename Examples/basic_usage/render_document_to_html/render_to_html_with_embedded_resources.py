# This example demonstrates how to render a document into HTML with embedded resources.

import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import os
from os.path import join
import test_files
import utils

def run():
    output_directory = join(utils.get_output_directory_path(), "render_to_html_with_embedded_resources")
    page_file_path_format = join(output_directory, "page_{0}.html")

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with gv.Viewer(test_files.sample_docx) as viewer:
        html_options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)

        viewer.view(html_options)

    print(f"\nSource document rendered successfully.\nCheck output in: {output_directory}")

if __name__ == "__main__":
    run()
