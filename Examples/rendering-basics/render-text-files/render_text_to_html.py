from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_text_to_html():
    # Load text file
    with Viewer("terms_of_service.txt") as viewer:
        # Convert the text file to HTML.
        # {0} is replaced with the current page number in the output file names.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_text_to_html/pdf_page_{0}.html")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_text_to_html()