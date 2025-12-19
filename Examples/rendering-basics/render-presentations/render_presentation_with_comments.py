from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_presentation_with_comments():
    # Load presentation
    with Viewer("sample.pptx") as viewer:
        viewOptions = PdfViewOptions("render_presentation_with_comments/presentation_with_comments.pdf")
        viewOptions.render_comments = True
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_presentation_with_comments()