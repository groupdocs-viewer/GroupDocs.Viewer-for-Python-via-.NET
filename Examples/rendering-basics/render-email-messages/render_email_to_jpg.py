from groupdocs.viewer import Viewer
from groupdocs.viewer.options import JpgViewOptions

def render_email_to_jpg():
    # Load email message
    with Viewer("sample.eml") as viewer:
        # Create a JPG file.
        viewOptions = JpgViewOptions("render_email_to_jpg/email_to_jpg.jpg")
        # Set width and height.
        viewOptions.width = 800
        viewOptions.height = 1000
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_email_to_jpg()