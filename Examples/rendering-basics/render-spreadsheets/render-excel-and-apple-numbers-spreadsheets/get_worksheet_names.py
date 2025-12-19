from groupdocs.viewer import Viewer
from groupdocs.viewer.options import ViewInfoOptions, SpreadsheetOptions

def get_worksheet_names():
    # Load Excel spreadsheet
    with Viewer("sample.xlsx") as viewer:
        view_info_options = ViewInfoOptions.for_html_view()
        # Call this method to create a single page for each worksheet.
        view_info_options.spreadsheet_options = SpreadsheetOptions.for_one_page_per_sheet()
        view_info = viewer.get_view_info(view_info_options)
        # Print the worksheet names in the console window.
        print("Worksheets:")
        for page in view_info.pages:
            print(f" - Worksheet {page.number} name '{page.name}'")

if __name__ == "__main__":
    get_worksheet_names()