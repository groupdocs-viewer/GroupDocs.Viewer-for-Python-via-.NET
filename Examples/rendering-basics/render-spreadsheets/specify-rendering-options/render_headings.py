from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_headings():
    # Load spreadsheet
    with Viewer("invoice.xlsx") as viewer:
        # Convert the spreadsheet to PDF.
        viewOptions = PdfViewOptions("render_headings/headings.pdf")
        # Render row and column headings.
        viewOptions.spreadsheet_options.render_headings = True
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_headings()