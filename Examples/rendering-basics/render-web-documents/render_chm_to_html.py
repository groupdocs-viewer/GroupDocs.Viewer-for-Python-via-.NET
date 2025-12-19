from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_chm_to_html():
    # Load CHM file
    with Viewer("sample.chm") as viewer:
        # Convert the CHM file to HTML.
        # {0} is replaced with the page numbers in the output file names.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_chm_to_html/chm_result_{0}.html")
        # Enable the following option to display all CHM content on a single HTML page.
        # viewOptions.render_to_single_page = True
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_chm_to_html()