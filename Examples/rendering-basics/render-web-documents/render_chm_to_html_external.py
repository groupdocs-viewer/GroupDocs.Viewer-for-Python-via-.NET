from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_chm_to_html_external():
    # Load CHM file
    with Viewer("sample.chm") as viewer:
        # Convert the CHM file to HTML.
        # Specify the output file names and location of external resources.
        viewOptions = HtmlViewOptions.for_external_resources("render_chm_to_html_external/pdf_page_{0}.html", "render_chm_to_html_external/pdf_page_{0}/resource_{0}_{1}", "render_chm_to_html_external/pdf_page_{0}/resource_{0}_{1}")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_chm_to_html_external()