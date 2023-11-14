# limit_count_of_items_to_render.py
# This example demonstrates how to limit the count of items when rendering Outlook data files.

import aspose.groupdocsviewer as gv
import aspose.groupdocsviewer.options as gvo
import os
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = os.path.join(output_directory, "page_{0}.html")

    with gv.Viewer(test_files.sample_ost) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        options.outlook_options.max_items_in_folder = 3

        viewer.view(options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
