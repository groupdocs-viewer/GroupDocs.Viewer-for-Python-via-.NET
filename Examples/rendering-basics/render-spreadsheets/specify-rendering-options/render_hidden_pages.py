from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_hidden_pages():
    # Load spreadsheet
    with Viewer("invoice.xlsx") as viewer:
        # Convert the spreadsheet to PDF.
        viewOptions = PdfViewOptions("render_hidden_pages/hidden_pages.pdf")
        # Enable rendering hidden pages.
        viewOptions.render_hidden_pages = True
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_hidden_pages()