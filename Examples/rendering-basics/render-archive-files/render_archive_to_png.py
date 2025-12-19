from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PngViewOptions

def render_archive_to_png():
    # Load archive file
    with Viewer("documents.zip") as viewer:
        # Create a PNG image for the top folder and each subfolder in the archive.
        # {0} is replaced with the current page number in the image name.
        viewOptions = PngViewOptions("render_archive_to_png/archive_page_0_{0}.png")
        # Set width and height.
        viewOptions.width = 800
        viewOptions.height = 1000
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_archive_to_png()