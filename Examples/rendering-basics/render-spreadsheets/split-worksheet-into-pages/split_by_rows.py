from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions, SpreadsheetOptions

def split_by_rows():
    # Load spreadsheet
    with Viewer("two-pages.xlsx") as viewer:
        # Specify number of rows for every page.
        rows_per_page = 15
        # Convert the spreadsheet to PDF.
        viewOptions = PdfViewOptions("split_by_rows/by_rows.pdf")
        # Split by number of rows.
        viewOptions.spreadsheet_options = SpreadsheetOptions.for_split_sheet_into_pages(rows_per_page)
        viewer.view(viewOptions)

if __name__ == "__main__":
    split_by_rows()