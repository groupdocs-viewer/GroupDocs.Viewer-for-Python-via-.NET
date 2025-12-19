from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_cad_to_html_external():
    # Load CAD file
    with Viewer("sample.dwg") as viewer:
        # Create an HTML file for the drawing.
        # Specify the HTML file name and location of external resources.
        # {0} is replaced with the resource name.
        viewOptions = HtmlViewOptions.for_external_resources("render_cad_to_html_external/pdf_page_{0}.html", "render_cad_to_html_external/pdf_page_{0}/resource_{0}_{1}", "render_cad_to_html_external/pdf_page_{0}/resource_{0}_{1}")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_cad_to_html_external()