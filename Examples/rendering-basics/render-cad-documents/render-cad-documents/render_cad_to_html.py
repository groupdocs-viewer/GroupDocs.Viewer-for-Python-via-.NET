from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_cad_to_html():
    # Load CAD file
    with Viewer("sample.dwg") as viewer:
        # Create an HTML file for the drawing.
        # Specify the HTML file name.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_cad_to_html/pdf_page_{0}.html")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_cad_to_html()