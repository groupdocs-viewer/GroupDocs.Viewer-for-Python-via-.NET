# skip_rendering_of_empty_rows.py
# This example demonstrates how to skip rendering of empty rows.

import os
from os.path import join
import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = join(output_directory, "page_{0}.html")

    with gv.Viewer(test_files.sample_xlsx_with_empty_row) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        options.spreadsheet_options.skip_empty_rows = True
        viewer.view(options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
