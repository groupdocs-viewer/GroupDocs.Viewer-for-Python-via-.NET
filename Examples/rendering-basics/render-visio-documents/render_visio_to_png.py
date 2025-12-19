from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PngViewOptions

def render_visio_to_png():
    # Load Visio document
    with Viewer("sample.vsdx") as viewer:
        # Create a PNG image for each drawing page.
        # {0} is replaced with the current page number in the image name.
        viewOptions = PngViewOptions("render_visio_to_png/visio_page_0_{0}.png")
        # Set width and height.
        viewOptions.width = 950
        viewOptions.height = 800
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_visio_to_png()