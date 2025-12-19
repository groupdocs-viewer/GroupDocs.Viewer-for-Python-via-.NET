from groupdocs.viewer import Viewer
from groupdocs.viewer.options import JpgViewOptions

def render_archive_to_jpg():
    # Load archive file
    with Viewer("documents.zip") as viewer:
        # Create a JPEG image for the top folder and each subfolder in the archive.
        # {0} is replaced with the current page number in the image name.
        viewOptions = JpgViewOptions("render_archive_to_jpg/archive_to_jpg_{0}.jpg")
        # Set width and height.
        viewOptions.width = 800
        viewOptions.height = 1000
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_archive_to_jpg()