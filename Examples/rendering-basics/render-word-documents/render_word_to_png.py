from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PngViewOptions

def render_word_to_png():
    # Load Word document
    with Viewer("sample.docx") as viewer:
        # Create a PNG image for each document page.
        # {0} is replaced with the current page number in the image name.
        viewOptions = PngViewOptions("render_word_to_png/word_page_0_{0}.png")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_word_to_png()