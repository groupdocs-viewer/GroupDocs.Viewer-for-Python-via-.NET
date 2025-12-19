from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions, SpreadsheetOptions

def split_by_page_breaks():
    # Load spreadsheet
    with Viewer("products.xlsx") as viewer:
        # Convert the spreadsheet to PDF.
        viewOptions = PdfViewOptions("split_by_page_breaks/by_page_breaks.pdf")
        # Split using page breaks.
        viewOptions.spreadsheet_options = SpreadsheetOptions.for_rendering_by_page_breaks()
        viewer.view(viewOptions)

if __name__ == "__main__":
    split_by_page_breaks()