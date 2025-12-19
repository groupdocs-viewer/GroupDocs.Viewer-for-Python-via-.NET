from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PngViewOptions

def render_pdf_to_png():
    # Load PDF document
    with Viewer("sample.pdf") as viewer:
        # Create a PNG image for each PDF page.
        # {0} is replaced with the current page number in the image name.
        viewOptions = PngViewOptions("render_pdf_to_png/pdf_page_{0}.png")
        # Set width and height.
        viewOptions.width = 950
        viewOptions.height = 550
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_pdf_to_png()