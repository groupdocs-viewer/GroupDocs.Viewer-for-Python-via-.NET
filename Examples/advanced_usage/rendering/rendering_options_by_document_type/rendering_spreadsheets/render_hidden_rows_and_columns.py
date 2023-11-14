# render_hidden_rows_and_columns.py
# This example demonstrates how to render hidden rows and columns.

import os
import aspose.groupdocsviewer as gv
import aspose.groupdocsviewer.options as gvo
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = os.path.join(output_directory, "page_{0}.html")

    with gv.Viewer(test_files.sample_xlsx_with_hidden_row_and_column) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        options.spreadsheet_options.render_hidden_columns = True
        options.spreadsheet_options.render_hidden_rows = True

        viewer.view(options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
