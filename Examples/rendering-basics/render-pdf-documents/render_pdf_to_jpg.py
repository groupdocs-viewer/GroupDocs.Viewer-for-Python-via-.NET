from groupdocs.viewer import Viewer
from groupdocs.viewer.options import JpgViewOptions

def render_pdf_to_jpg():
    # Load PDF document
    with Viewer("sample.pdf") as viewer:
        # Create a JPG image for each PDF page.
        # {0} is replaced with the current page number in the image name.
        viewOptions = JpgViewOptions("render_pdf_to_jpg/pdf_to_jpg_{0}.jpg")
        # Set width and height.
        viewOptions.width = 950
        viewOptions.height = 550
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_pdf_to_jpg()