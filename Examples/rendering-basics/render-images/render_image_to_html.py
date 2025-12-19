from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_image_to_html():
    # Load image
    with Viewer("vector-image.svg") as viewer:
        # Specify the HTML file name.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_image_to_html/pdf_page_{0}.html")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_image_to_html()