from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions, SpreadsheetOptions

def split_by_rows_and_columns():
    # Load spreadsheet
    with Viewer("four-pages.xlsx") as viewer:
        # Specify number of rows and columns for every page.
        rows_per_page = 15
        column_per_page = 7
        # Convert the spreadsheet to PDF.
        viewOptions = PdfViewOptions("split_by_rows_and_columns/by_rows_and_columns.pdf")
        # Split by number of rows and columns.
        viewOptions.spreadsheet_options = SpreadsheetOptions.for_split_sheet_into_pages(rows_per_page, column_per_page)
        viewer.view(viewOptions)

if __name__ == "__main__":
    split_by_rows_and_columns()