from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_archive_with_items_per_page():
    # Load archive file
    with Viewer("documents.zip") as viewer:
        # Create an HTML file for the top folder and each subfolder in the archive.
        # {0} is replaced with the current page number in the output file name.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_archive_with_items_per_page/archive_with_items_per_page_{0}.html")
        # Specify the number of items to display on each HTML page.
        viewOptions.archive_options.items_per_page = 10
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_archive_with_items_per_page()