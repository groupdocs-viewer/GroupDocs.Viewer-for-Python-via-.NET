from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_excel_to_single_html():
    # Load Excel spreadsheet
    with Viewer("invoice.xlsx") as viewer:
        # Convert all Excel worksheets to one HTML file.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_excel_to_single_html/page.html")
        # Enable converting all worksheets to one file.
        viewOptions.render_to_single_page = True
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_excel_to_single_html()