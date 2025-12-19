from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions, SpreadsheetOptions

def render_print_area_and_page_breaks():
    # Load spreadsheet
    with Viewer("Products.xlsx") as viewer:
        # Render the spreadsheet to PDF.
        viewOptions = PdfViewOptions("render_print_area_and_page_breaks/print_area_and_page_breaks.pdf")
        viewOptions.spreadsheet_options = SpreadsheetOptions.for_rendering_print_area_and_page_breaks()
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_print_area_and_page_breaks()