from groupdocs.viewer import Viewer
from groupdocs.viewer.options import JpgViewOptions

def render_image_to_jpg():
    # Load image
    with Viewer("vector-image.svg") as viewer:
        # Create a JPG image.
        viewOptions = JpgViewOptions("render_image_to_jpg/image_to_jpg.jpg")
        # Set width and height.
        viewOptions.width = 950
        viewOptions.height = 550
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_image_to_jpg()