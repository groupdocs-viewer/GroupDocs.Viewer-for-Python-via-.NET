from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PngViewOptions

def render_web_to_png():
    # Load web document
    with Viewer("groupdocs-documentation.mhtml") as viewer:
        # Convert the web file to PNG.
        # {0} is replaced with the page numbers in the output image names.
        viewOptions = PngViewOptions("render_web_to_png/optimized_for_web_{0}.pdf")
        # Set width and height.
        viewOptions.width = 950
        viewOptions.height = 800
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_web_to_png()