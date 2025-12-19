from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_text_to_pdf():
    # Load text file
    with Viewer("terms_of_service.txt") as viewer:
        # Convert the text file to PDF.
        viewOptions = PdfViewOptions("render_text_to_pdf/text_document.pdf")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_text_to_pdf()