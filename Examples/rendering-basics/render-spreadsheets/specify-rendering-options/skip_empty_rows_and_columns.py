from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def skip_empty_rows_and_columns():
    # Load spreadsheet
    with Viewer("invoice.xlsx") as viewer:
        # Convert the spreadsheet to PDF.
        viewOptions = PdfViewOptions("skip_empty_rows_and_columns/skip_empty_rows_and_columns.pdf")
        # Enable skipping blank rows and columns.
        viewOptions.spreadsheet_options.skip_empty_columns = True
        viewOptions.spreadsheet_options.skip_empty_rows = True
        viewer.view(viewOptions)

if __name__ == "__main__":
    skip_empty_rows_and_columns()