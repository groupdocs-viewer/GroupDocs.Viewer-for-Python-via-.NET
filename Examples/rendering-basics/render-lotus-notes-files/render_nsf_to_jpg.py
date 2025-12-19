from groupdocs.viewer import Viewer
from groupdocs.viewer.options import JpgViewOptions

def render_nsf_to_jpg():
    # Load NSF file
    with Viewer("sample.nsf") as viewer:
        # Convert the NSF file to JPEG.
        # {0} is replaced with the page numbers in the output image names.
        viewOptions = JpgViewOptions("render_nsf_to_jpg/nsf_to_jpg_{0}.jpg")
        # Set width and height.
        viewOptions.width = 800
        viewOptions.height = 1000
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_nsf_to_jpg()