from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PngViewOptions

def render_email_to_png():
    # Load email message
    with Viewer("sample.eml") as viewer:
        # Create a PNG file.
        viewOptions = PngViewOptions("render_email_to_png/email_page_0.png")
        # Set width and height.
        viewOptions.width = 800
        viewOptions.height = 1000
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_email_to_png()