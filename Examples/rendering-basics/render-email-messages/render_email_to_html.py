from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_email_to_html():
    # Load email message
    with Viewer("sample.eml") as viewer:
        # Create an HTML file.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_email_to_html/pdf_page_{0}.html")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_email_to_html()