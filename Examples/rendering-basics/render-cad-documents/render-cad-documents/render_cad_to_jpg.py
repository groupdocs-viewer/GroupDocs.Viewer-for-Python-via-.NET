from groupdocs.viewer import Viewer
from groupdocs.viewer.options import JpgViewOptions

def render_cad_to_jpg():
    # Load CAD file
    with Viewer("sample.dwg") as viewer:
        # Create a JPG image for the drawing.
        viewOptions = JpgViewOptions("render_cad_to_jpg/cad_to_jpg.jpg")
        # Set width and height.
        viewOptions.width = 1500
        viewOptions.height = 1000
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_cad_to_jpg()