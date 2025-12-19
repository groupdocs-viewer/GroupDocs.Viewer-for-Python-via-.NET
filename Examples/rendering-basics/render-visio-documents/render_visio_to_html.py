from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_visio_to_html():
    # Load Visio document
    with Viewer("sample.vsdx") as viewer:
        # Create an HTML file for each drawing page.
        # {0} is replaced with the current page number in the file name.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_visio_to_html/pdf_page_{0}.html")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_visio_to_html()