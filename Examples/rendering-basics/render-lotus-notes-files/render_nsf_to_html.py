from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_nsf_to_html():
    # Load NSF file
    with Viewer("sample.nsf") as viewer:
        # Create an HTML file.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_nsf_to_html/pdf_page_{0}.html")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_nsf_to_html()