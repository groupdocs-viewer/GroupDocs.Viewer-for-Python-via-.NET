# rendering_by_page_breaks.py
# This example demonstrates how to render spreadsheets by page breaks.

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

    output_file_path = join(output_directory, "output.pdf")

    with gv.Viewer(test_files.page_breaks_xlsx) as viewer:
        options = gvo.PdfViewOptions(output_file_path)
        options.spreadsheet_options = gvo.SpreadsheetOptions.for_rendering_by_page_breaks()

        # Enable rendering grid lines and headings to check that proper areas are rendered
        options.spreadsheet_options.render_grid_lines = True
        options.spreadsheet_options.render_headings = True

        viewer.view(options)

    # Indicate the successful rendering of the source document and specify where to find the output in the specified directory
    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}")

if __name__ == "__main__":
    run()
