from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_visio_shapes_only():
    # Load Visio document
    with Viewer("map.vsdx") as viewer:
        # Convert the Visio file to PDF.
        viewOptions = PdfViewOptions("render_visio_shapes_only/visio_shapes_only.pdf")
        # Render the master shapes only.
        viewOptions.visio_rendering_options.render_figures_only = True
        # Specify shape width in pixels.
        viewOptions.visio_rendering_options.figure_width = 200
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_visio_shapes_only()