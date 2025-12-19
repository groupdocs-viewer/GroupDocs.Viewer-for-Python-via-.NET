from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_excel_to_html():
    # Load Excel spreadsheet
    with Viewer("invoice.xlsx") as viewer:
        # Convert the spreadsheet to HTML.
        # {0} is replaced with the current page number in the file names.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_excel_to_html/pdf_page_{0}.html")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_excel_to_html()