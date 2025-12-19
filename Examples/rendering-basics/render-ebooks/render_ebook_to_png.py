from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PngViewOptions

def render_ebook_to_png():
    # Load EBook
    with Viewer("sample.epub") as viewer:
        # Create a PNG image for each document page.
        # {0} is replaced with the current page number in the image name.
        viewOptions = PngViewOptions("render_ebook_to_png/ebook_page_0_{0}.png")
        # Set width and height.
        viewOptions.width = 800
        viewOptions.height = 900
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_ebook_to_png()