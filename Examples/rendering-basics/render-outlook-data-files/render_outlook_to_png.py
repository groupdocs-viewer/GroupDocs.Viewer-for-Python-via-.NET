from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PngViewOptions

def render_outlook_to_png():
    # Load Outlook data file
    with Viewer("sample.pst") as viewer:
        # Convert the PST file to PNG.
        # {0} is replaced with the page numbers in the output image names.
        viewOptions = PngViewOptions("render_outlook_to_png/outlook_page_0_{0}.png")
        # Set width and height.
        viewOptions.width = 800
        viewOptions.height = 900
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_outlook_to_png()