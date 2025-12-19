from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_archive_to_single_html():
    # Load archive file
    with Viewer("documents.zip") as viewer:
        # Create an HTML file.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_archive_to_single_html/archive_to_single_html.html")
        # Render the archive file to a single page.
        viewOptions.render_to_single_page = True
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_archive_to_single_html()