from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PngViewOptions

def render_pdf_with_comments():
    # Load PDF document
    with Viewer("sample.pdf") as viewer:
        # Create a PNG image for each PDF page.
        # {0} is replaced with the current page number in the image name.
        viewOptions = PngViewOptions("render_pdf_with_comments/pdf_with_comments_{0}.png")
        # Enable rendering comments.
        viewOptions.render_comments = True
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_pdf_with_comments()