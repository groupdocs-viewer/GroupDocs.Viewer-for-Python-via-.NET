# set_resource_loading_timeout.py
# This example demonstrates how to set a timeout for loading external resources contained by a document.

import os
from datetime import timedelta
import aspose.groupdocsviewer as gv
import aspose.groupdocsviewer.options as gvo
import test_files
import utils

def run():    
    output_directory = utils.get_output_directory_path()
    page_file_path_format = os.path.join(output_directory, "page_{0}.html")

    load_options = gvo.LoadOptions()
    load_options.resource_loading_timeout = timedelta(seconds=5)

    with gv.Viewer(test_files.with_external_image_doc, load_options) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        viewer.view(options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
