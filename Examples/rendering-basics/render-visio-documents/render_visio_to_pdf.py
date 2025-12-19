from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_visio_to_pdf():
    # Load Visio document
    with Viewer("sample.vsdx") as viewer:
        # Create a PDF file for the document.
        # Specify the PDF file name.
        viewOptions = PdfViewOptions("render_visio_to_pdf/visio_diagram.pdf")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_visio_to_pdf()