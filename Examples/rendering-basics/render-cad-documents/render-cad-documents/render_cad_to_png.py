from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PngViewOptions

def render_cad_to_png():
    # Load CAD file
    with Viewer("sample.dwg") as viewer:
        # Create a PNG image for the drawing.
        viewOptions = PngViewOptions("render_cad_to_png/cad_page_0.png")
        # Set width and height.
        viewOptions.width = 1500
        viewOptions.height = 1000
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_cad_to_png()