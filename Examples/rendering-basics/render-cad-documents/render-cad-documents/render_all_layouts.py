from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_all_layouts():
    # Load CAD file
    with Viewer("sample.dwg") as viewer:
        # Convert the document to PDF.
        options = PdfViewOptions("render_all_layouts/all_layouts.pdf")
        # Render the Model and all non-empty paper space layouts. 
        options.cad_options.render_layouts = True
        viewer.view(options)

if __name__ == "__main__":
    render_all_layouts()