from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_presentation_to_pdf():
    # Load presentation
    with Viewer("sample.pptx") as viewer:
        viewOptions = PdfViewOptions("render_presentation_to_pdf/presentation.pdf")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_presentation_to_pdf()