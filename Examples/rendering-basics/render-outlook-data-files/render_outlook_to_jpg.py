from groupdocs.viewer import Viewer
from groupdocs.viewer.options import JpgViewOptions

def render_outlook_to_jpg():
    # Load Outlook data file
    with Viewer("sample.pst") as viewer:
        # Convert the PST file to JPEG.
        # {0} is replaced with the page numbers in the output image names.
        viewOptions = JpgViewOptions("render_outlook_to_jpg/outlook_to_jpg_{0}.jpg")
        # Set width and height.
        viewOptions.width = 800
        viewOptions.height = 900
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_outlook_to_jpg()