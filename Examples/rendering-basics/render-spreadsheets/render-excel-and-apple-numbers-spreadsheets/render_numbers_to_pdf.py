from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_numbers_to_pdf():
    # Load Apple Numbers spreadsheet
    with Viewer("sample.numbers") as viewer:
        # Convert the spreadsheet to PDF.
        viewOptions = PdfViewOptions("render_numbers_to_pdf/spreadsheet.pdf")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_numbers_to_pdf()