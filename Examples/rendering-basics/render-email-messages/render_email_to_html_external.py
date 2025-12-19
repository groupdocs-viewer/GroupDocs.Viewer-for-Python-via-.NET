from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_email_to_html_external():
    # Load email message
    with Viewer("sample.eml") as viewer:
        # Specify the HTML file name and location of external resources.
        # {0} is replaced with the resource name in the output file name.
        viewOptions = HtmlViewOptions.for_external_resources("render_email_to_html_external/pdf_page_{0}.html", "render_email_to_html_external/pdf_page_{0}/resource_{0}_{1}", "render_email_to_html_external/pdf_page_{0}/resource_{0}_{1}")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_email_to_html_external()