from groupdocs.viewer import Viewer
from groupdocs.viewer.options import JpgViewOptions

def render_web_to_jpg():
    # Load web document
    with Viewer("groupdocs-documentation.mhtml") as viewer:
        # Create a JPEG image for each page.
        # {0} is replaced with the current page number in the image name.
        viewOptions = JpgViewOptions("render_web_to_jpg/web_to_jpg_{0}.jpg")
        # Set width and height.
        viewOptions.width = 1600
        viewOptions.height = 650
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_web_to_jpg()