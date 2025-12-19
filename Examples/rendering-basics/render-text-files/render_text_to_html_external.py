from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_text_to_html_external():
    # Load text file
    with Viewer("terms_of_service.txt") as viewer:
        # Create an HTML file for each page.
        # Specify the HTML file names and location of external resources.
        # {0} and {1} are replaced with the current page number and resource name, respectively.
        viewOptions = HtmlViewOptions.for_external_resources("render_text_to_html_external/pdf_page_{0}.html", "render_text_to_html_external/pdf_page_{0}/resource_{0}_{1}", "render_text_to_html_external/pdf_page_{0}/resource_{0}_{1}")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_text_to_html_external()