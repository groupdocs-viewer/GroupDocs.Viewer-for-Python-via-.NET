from groupdocs.viewer import Viewer
from groupdocs.viewer.options import JpgViewOptions

def render_ebook_to_jpg():
    # Load EBook
    with Viewer("sample.epub") as viewer:
        # Create a JPEG image for each document page.
        # {0} is replaced with the current page number in the image name.
        viewOptions = JpgViewOptions("render_ebook_to_jpg/ebook_to_jpg_{0}.jpg")
        # Set width and height.
        viewOptions.width = 800
        viewOptions.height = 900
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_ebook_to_jpg()