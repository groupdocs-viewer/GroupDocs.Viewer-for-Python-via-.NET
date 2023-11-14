# render_all_layouts.py
# This example demonstrates how to render all layouts.

import aspose.groupdocsviewer as gv
import aspose.groupdocsviewer.options as gvo
import os
from os.path import join
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = join(output_directory, "page_{0}.html")

    with gv.Viewer(test_files.sample_dwg_with_layouts_and_layers) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        options.cad_options.render_layouts = True

        viewer.view(options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}")

if __name__ == "__main__":
    run()
