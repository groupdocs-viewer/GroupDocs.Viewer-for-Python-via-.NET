from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_word_to_html():
    # Load Word document
    with Viewer("sample.docx") as viewer:
        # Create an HTML files.
        # {0} is replaced with the current page number in the file name.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_word_to_html/pdf_page_{0}.html")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_word_to_html()