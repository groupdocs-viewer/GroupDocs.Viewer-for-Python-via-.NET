from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions, SpreadsheetOptions

def render_print_area():
    # Load spreadsheet
    with Viewer("invoice.xlsx") as viewer:
        # Convert the spreadsheet to PDF.
        viewOptions = PdfViewOptions("render_print_area/print_area.pdf")
        # Render the print area only.
        viewOptions.spreadsheet_options = SpreadsheetOptions.for_rendering_print_area()
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_print_area()