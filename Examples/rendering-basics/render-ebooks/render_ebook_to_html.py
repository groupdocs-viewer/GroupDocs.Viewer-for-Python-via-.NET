from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_ebook_to_html():
    # Load EBook
    with Viewer("sample.epub") as viewer:
        # Create an HTML file for each document page.
        # {0} is replaced with the current page number in the file name.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_ebook_to_html/pdf_page_{0}.html")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_ebook_to_html()