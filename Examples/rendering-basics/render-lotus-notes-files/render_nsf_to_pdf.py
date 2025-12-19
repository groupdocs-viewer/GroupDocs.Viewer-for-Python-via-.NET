from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_nsf_to_pdf():
    # Load NSF file
    with Viewer("sample.nsf") as viewer:
        # Create a PDF file.
        viewOptions = PdfViewOptions("render_nsf_to_pdf/lotus_notes.pdf")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_nsf_to_pdf()