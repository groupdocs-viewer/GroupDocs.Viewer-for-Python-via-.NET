from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PngViewOptions

def render_nsf_to_png():
    # Load NSF file
    with Viewer("sample.nsf") as viewer:
        # Convert the NSF file to PNG.
        # {0} is replaced with the page numbers in the output image names.
        viewOptions = PngViewOptions("render_nsf_to_png/lotus_notes_page_0_{0}.png")
        # Set width and height.
        viewOptions.width = 800
        viewOptions.height = 1000
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_nsf_to_png()