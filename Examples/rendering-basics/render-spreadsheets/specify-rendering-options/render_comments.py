from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PngViewOptions

def render_comments():
    # Load spreadsheet
    with Viewer("invoice.xlsx") as viewer:
        # Convert the spreadsheet to PNG.
        # {0} is replaced with the current page number in the file names.
        viewOptions = PngViewOptions("render_comments/comments_{0}.png")
        # Enable rendering comments.
        viewOptions.render_comments = True
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_comments()