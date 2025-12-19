from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_excel_to_pdf():
    # Load Excel spreadsheet
    with Viewer("invoice.xlsx") as viewer:
        # Convert the spreadsheet to PDF.
        viewOptions = PdfViewOptions("render_excel_to_pdf/spreadsheet.pdf")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_excel_to_pdf()