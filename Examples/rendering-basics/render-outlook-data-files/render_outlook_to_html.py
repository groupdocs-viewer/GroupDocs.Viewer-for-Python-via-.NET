from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_outlook_to_html():
    # Load Outlook data file
    with Viewer("sample.pst") as viewer:
        # Create an HTML file.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_outlook_to_html/pdf_page_{0}.html")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_outlook_to_html()