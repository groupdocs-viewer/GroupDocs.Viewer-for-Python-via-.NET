from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_numbers_to_html():
    # Load Apple Numbers spreadsheet
    with Viewer("sample.numbers") as viewer:
        # Convert the spreadsheet to HTML.
        # {0} is replaced with the current page number in the file names.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_numbers_to_html/pdf_page_{0}.html")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_numbers_to_html()