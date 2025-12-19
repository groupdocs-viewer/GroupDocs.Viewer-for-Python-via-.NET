from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PngViewOptions

def render_pdf_with_font_hinting():
    # Load PDF document
    with Viewer("sample.pdf") as viewer:
        # Create a PNG image for each PDF page.
        # {0} is replaced with the current page number in the image name.
        viewOptions = PngViewOptions("render_pdf_with_font_hinting/pdf_with_font_hinting_{0}.png")
        # Enable font hinting
        viewOptions.pdf_options.enable_font_hinting = True
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_pdf_with_font_hinting()