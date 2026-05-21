from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions, SpreadsheetOptions

def render_one_page_per_sheet():
    # Load spreadsheet
    with Viewer("products.xlsx") as viewer:
        # Convert the spreadsheet to PDF.
        viewOptions = PdfViewOptions("render_one_page_per_sheet/one_page_per_sheet.pdf")
        # Render each worksheet to one page.
        viewOptions.spreadsheet_options = SpreadsheetOptions.for_one_page_per_sheet()
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_one_page_per_sheet()