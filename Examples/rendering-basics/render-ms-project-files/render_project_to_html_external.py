from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_project_to_html_external():
    # Load Project file
    with Viewer("sample.mpp") as viewer:
        # Render the project's active view as HTML.
        # Specify the HTML file names and location of external resources.
        # {0} and {1} are replaced with the page number and resource name, respectively.
        viewOptions = HtmlViewOptions.for_external_resources("render_project_to_html_external/pdf_page_{0}.html", "render_project_to_html_external/pdf_page_{0}/resource_{0}_{1}", "render_project_to_html_external/pdf_page_{0}/resource_{0}_{1}")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_project_to_html_external()