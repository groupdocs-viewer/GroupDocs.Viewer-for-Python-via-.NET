from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PngViewOptions

def render_numbers_to_png():
    # Load Apple Numbers spreadsheet
    with Viewer("sample.numbers") as viewer:
        # Convert the spreadsheet to PNG.
        # {0} is replaced with the current page number in the file names.
        viewOptions = PngViewOptions("render_numbers_to_png/spreadsheet_page_0_{0}.png")
        # Set width and height.
        viewOptions.width = 800
        viewOptions.height = 900
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_numbers_to_png()