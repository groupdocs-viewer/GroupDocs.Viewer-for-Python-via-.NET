from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions
from groupdocs.viewer.drawing import Argb32Color

def set_background_color():
    # Load CAD file
    with Viewer("sample.dwg") as viewer:
        viewOptions = PdfViewOptions("set_background_color/background_color.pdf")
        viewOptions.cad_options.background_color = Argb32Color.from_rgb(255, 255, 0)  # RGB color for yellow
        viewer.view(viewOptions)

if __name__ == "__main__":
    set_background_color()