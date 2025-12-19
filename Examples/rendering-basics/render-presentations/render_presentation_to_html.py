from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_presentation_to_html():
    # Load presentation
    with Viewer("sample.pptx") as viewer:
        # Create an HTML file for each slide.
        # {0} is replaced with the current page number in the file name.
        options = HtmlViewOptions.for_embedded_resources("render_presentation_to_html/pdf_page_{0}.html")
        viewer.view(options)

if __name__ == "__main__":
    render_presentation_to_html()