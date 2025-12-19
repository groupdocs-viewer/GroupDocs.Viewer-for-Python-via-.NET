from groupdocs.viewer import Viewer
from groupdocs.viewer.options import JpgViewOptions

def render_visio_to_jpg():
    # Load Visio document
    with Viewer("sample.vsdx") as viewer:
        # Create a JPEG image for each drawing page.
        # {0} is replaced with the current page number in the image name.
        viewOptions = JpgViewOptions("render_visio_to_jpg/visio_to_jpg_{0}.jpg")
        # Set width and height.
        viewOptions.width = 950
        viewOptions.height = 800
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_visio_to_jpg()