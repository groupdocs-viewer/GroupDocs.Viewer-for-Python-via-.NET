from groupdocs.viewer import Viewer
from groupdocs.viewer.options import JpgViewOptions

def render_text_to_jpg():
    # Load text file
    with Viewer("terms_of_service.txt") as viewer:
        # Convert the text file to JPEG.
        # {0} is replaced with the current page number in the output image names.
        viewOptions = JpgViewOptions("render_text_to_jpg/text_to_jpg_{0}.jpg")
        # Set width and height.
        viewOptions.width = 950
        viewOptions.height = 550
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_text_to_jpg()