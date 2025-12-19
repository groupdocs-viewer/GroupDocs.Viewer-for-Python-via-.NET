from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_cad_to_pdf():
    # Load CAD file
    with Viewer("sample.dwg") as viewer:
        # Create a PDF file for the drawing.
        # Specify the PDF file name.
        viewOptions = PdfViewOptions("render_cad_to_pdf/cad_drawing.pdf")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_cad_to_pdf()