from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions
from groupdocs.viewer.results import Layer

def render_specific_layers():
    # Load CAD file
    with Viewer("sample.dwg") as viewer:
        # Convert the document to PDF.
        options = PdfViewOptions("render_specific_layers/specific_layers.pdf")
        # Specify a list of layers to display.
        options.cad_options.layers = [
            Layer("QUADRANT")
        ]
        viewer.view(options)

if __name__ == "__main__":
    render_specific_layers()