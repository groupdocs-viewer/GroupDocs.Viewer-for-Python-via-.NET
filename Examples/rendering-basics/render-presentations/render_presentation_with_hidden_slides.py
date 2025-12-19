from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_presentation_with_hidden_slides():
    # Load presentation
    with Viewer("sample.pptx") as viewer:
        viewOptions = PdfViewOptions("render_presentation_with_hidden_slides/presentation_with_hidden_slides.pdf")
        viewOptions.render_hidden_pages = True
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_presentation_with_hidden_slides()