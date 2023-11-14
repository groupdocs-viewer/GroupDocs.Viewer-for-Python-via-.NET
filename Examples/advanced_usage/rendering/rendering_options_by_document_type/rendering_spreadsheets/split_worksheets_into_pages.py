# split_worksheets_into_pages.py
# This example demonstrates how to split worksheet(s) into page(s).

import os
from os.path import join
import aspose.groupdocsviewer as gv
import aspose.groupdocsviewer.options as gvo
import test_files
import utils

def split_by_rows():
    output_directory = join(utils.get_output_directory_path(), "SplitByRows")
    page_file_path_format = join(output_directory, "page_{0}.html")

    with gv.Viewer(test_files.two_pages_xlsx) as viewer:
        count_rows_per_page = 15
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        options.spreadsheet_options = gvo.SpreadsheetOptions.for_split_sheet_into_pages(count_rows_per_page)
        viewer.view(options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

def split_by_rows_and_columns():
    output_directory = join(utils.get_output_directory_path(), "SplitByRowsAndColumns")
    page_file_path_format = join(output_directory, "page_{0}.html")

    with gv.Viewer(test_files.four_pages_xlsx) as viewer:
        count_rows_per_page = 15
        count_columns_per_page = 7
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        options.spreadsheet_options = gvo.SpreadsheetOptions.for_split_sheet_into_pages(count_rows_per_page, count_columns_per_page)
        viewer.view(options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    split_by_rows()
    split_by_rows_and_columns()
