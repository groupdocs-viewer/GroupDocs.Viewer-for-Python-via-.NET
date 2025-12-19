from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PngViewOptions

def render_pdf_preserve_page_size():
    # Load PDF document
    with Viewer("sample.pdf") as viewer:
        # Create a PNG image for each PDF page.
        # {0} is replaced with the current page number in the image name.
        viewOptions = PngViewOptions("render_pdf_preserve_page_size/pdf_preserve_page_size_{0}.png")
        # Preserve the size of document pages.
        viewOptions.pdf_options.render_original_page_size = True
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_pdf_preserve_page_size()