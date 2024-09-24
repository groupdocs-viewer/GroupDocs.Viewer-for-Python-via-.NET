# get_worksheets_names.py
# This example demonstrates how to retrieve and print worksheets names.

import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import test_files

def run():
    with gv.Viewer(test_files.three_sheets) as viewer:
        view_info_options = gvo.ViewInfoOptions.for_html_view()
        view_info_options.spreadsheet_options = gvo.SpreadsheetOptions.for_one_page_per_sheet()

        view_info = viewer.get_view_info(view_info_options)

        print("Worksheets:")
        for page in view_info.pages:
            print(f" - Worksheet {page.number} name '{page.name}'")

if __name__ == "__main__":
    run()
