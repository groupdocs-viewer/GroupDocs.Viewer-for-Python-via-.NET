from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_image_to_pdf():
    # Load image
    with Viewer("vector-image.svg") as viewer:
        # Create a PDF file.
        viewOptions = PdfViewOptions("render_image_to_pdf/pdf_document.pdf")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_image_to_pdf()