from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PngViewOptions

def render_image_to_png():
    # Load image
    with Viewer("vector-image.svg") as viewer:
        # Create a PNG image.
        viewOptions = PngViewOptions("render_image_to_png/image.png")
        # Set width and height.
        viewOptions.width = 950
        viewOptions.height = 550
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_image_to_png()