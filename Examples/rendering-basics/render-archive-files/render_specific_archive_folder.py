from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_specific_archive_folder():

    # Load archive file
    with Viewer("documents.zip") as viewer:
        # Create an HTML file.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_specific_archive_folder/specific_archive_folder.html")
        viewOptions.archive_options.folder = "first_folder"
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_specific_archive_folder()