from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_presentation_with_notes():
    # Load presentation
    with Viewer("sample.pptx") as viewer:
        viewOptions = PdfViewOptions("render_presentation_with_notes/presentation_with_notes.pdf")
        viewOptions.render_notes = True
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_presentation_with_notes()