from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_web_to_pdf():
    # Load web document
    with Viewer("groupdocs-documentation.mhtml") as viewer:
        # Create a PDF file for the document.
        # Specify the PDF file name.
        viewOptions = PdfViewOptions("render_web_to_pdf/optimized_for_web.pdf")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_web_to_pdf()