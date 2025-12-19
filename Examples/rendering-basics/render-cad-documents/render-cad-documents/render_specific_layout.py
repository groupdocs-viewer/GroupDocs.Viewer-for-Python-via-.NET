from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_specific_layout():
    # Load CAD file
    with Viewer("sample.dwg") as viewer:
        # Convert the document to PDF.
        options = PdfViewOptions("render_specific_layout/specific_layout.pdf")
        # Specify the name of the layout to render.
        # If the specified layout is not found,
        # an exception occurs.
        options.cad_options.layout_name = "layout1"
        viewer.view(options)

if __name__ == "__main__":
    render_specific_layout()