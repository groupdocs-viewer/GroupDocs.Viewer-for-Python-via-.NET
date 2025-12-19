from groupdocs.viewer import Viewer
from groupdocs.viewer.options import JpgViewOptions

def render_presentation_to_jpg():
    # Load presentation
    with Viewer("sample.pptx") as viewer:
        # Create a JPG image for each slide.
        # {0} is replaced with the current page number in the image name.
        viewOptions = JpgViewOptions("render_presentation_to_jpg/presentation_to_jpg_{0}.jpg")
        viewOptions.width = 950
        viewOptions.height = 550
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_presentation_to_jpg()