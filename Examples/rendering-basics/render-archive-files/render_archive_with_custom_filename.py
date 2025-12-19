from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions, FileName

def render_archive_with_custom_filename():
    # Load archive file
    with Viewer("documents.zip") as viewer:
        # Create an HTML file for the top folder and each subfolder in the archive.
        # {0} is replaced with the current page number in the output file name.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_archive_with_custom_filename/archive_with_custom_filename_{0}.html")
        # Specify a custom filename
        viewOptions.archive_options.file_name = FileName("Sample Files")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_archive_with_custom_filename()