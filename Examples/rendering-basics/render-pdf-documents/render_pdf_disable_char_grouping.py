from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PngViewOptions

def render_pdf_disable_char_grouping():
    # Load PDF document
    with Viewer("sample.pdf") as viewer:
        # Create a PNG image for each PDF page.
        # {0} is replaced with the current page number in the image name.
        viewOptions = PngViewOptions("render_pdf_disable_char_grouping/pdf_disable_char_grouping_{0}.png")
        # Disable character grouping.
        viewOptions.pdf_options.disable_chars_grouping = True
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_pdf_disable_char_grouping()