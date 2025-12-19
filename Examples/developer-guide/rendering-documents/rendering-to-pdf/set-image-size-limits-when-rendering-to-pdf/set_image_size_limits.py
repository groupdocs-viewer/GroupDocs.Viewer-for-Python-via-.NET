from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def set_image_size_limits():
    # Load document
    with Viewer("sample.jpg") as viewer:
        # Create a PDF file.
        viewOptions = PdfViewOptions("set_image_size_limits/image_with_size_limits.pdf")

        # Specify the maximum width and height.
        viewOptions.image_max_width = 800
        viewOptions.image_max_height = 600
        viewer.view(viewOptions)

if __name__ == "__main__":
    set_image_size_limits()