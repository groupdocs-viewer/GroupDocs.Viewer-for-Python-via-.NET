from groupdocs.viewer import Viewer
from groupdocs.viewer.options import JpgViewOptions

def render_excel_to_jpg():
    # Load Excel spreadsheet
    with Viewer("invoice.xlsx") as viewer:
        # Convert the spreadsheet to JPEG.
        # {0} is replaced with the current page number in the file names.
        viewOptions = JpgViewOptions("render_excel_to_jpg/excel_to_jpg_{0}.jpg")
        # Set width and height.
        viewOptions.width = 800
        viewOptions.height = 900
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_excel_to_jpg()