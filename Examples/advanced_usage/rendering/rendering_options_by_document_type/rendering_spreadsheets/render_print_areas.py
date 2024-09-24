# render_print_areas.py
# This example demonstrates how to render print area(s).

import os
import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = os.path.join(output_directory, "page_{0}.html")

    with gv.Viewer(test_files.sample_xlsx_with_print_areas) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        options.spreadsheet_options = gvo.SpreadsheetOptions.for_rendering_print_area()

        viewer.view(options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
