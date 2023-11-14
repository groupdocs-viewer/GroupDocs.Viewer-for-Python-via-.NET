# This example demonstrates how to render a document into HTML with external resources.

import aspose.groupdocsviewer as gv
import aspose.groupdocsviewer.options as gvo
import os
from os.path import join
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()

    # The {0} and {1} patterns will be replaced with the current processing page number and resource name accordingly.
    page_file_path_format = join(output_directory, "page_{0}.html")
    resource_file_path_format = join(output_directory, "page_{0}_{1}")
    resource_url_format = join(output_directory, "page_{0}_{1}")

    with gv.Viewer(test_files.sample_docx) as viewer:
        html_options = gvo.HtmlViewOptions.for_external_resources(
            page_file_path_format, resource_file_path_format, resource_url_format
        )

        viewer.view(html_options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
