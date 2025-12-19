from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PngViewOptions

def render_presentation_to_png():
    # Load presentation
    with Viewer("sample.pptx") as viewer:
        # Create a PNG image for each slide.
        # {0} is replaced with the current page number in the image name.
        viewOptions = PngViewOptions("render_presentation_to_png/presentation_page_0_{0}.png")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_presentation_to_png()