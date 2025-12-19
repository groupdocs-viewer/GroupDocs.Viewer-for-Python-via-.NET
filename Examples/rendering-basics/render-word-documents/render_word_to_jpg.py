from groupdocs.viewer import Viewer
from groupdocs.viewer.options import JpgViewOptions

def render_word_to_jpg():
    # Load Word document
    with Viewer("sample.docx") as viewer:
        # Create a JPG image for each document page.
        # {0} is replaced with the current page number in the image name.
        viewOptions = JpgViewOptions("render_word_to_jpg/word_to_jpg_{0}.jpg")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_word_to_jpg()