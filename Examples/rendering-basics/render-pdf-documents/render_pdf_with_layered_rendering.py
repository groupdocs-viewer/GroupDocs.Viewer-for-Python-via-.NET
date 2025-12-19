from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_pdf_with_layered_rendering():
    # Load PDF document
    with Viewer("sample.pdf") as viewer:
        # Create an HTML files.
        # {0} is replaced with the current page number in the file name.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_pdf_with_layered_rendering/pdf_with_layered_rendering_{0}.html")
        # Enable the multi-layer rendering.
        viewOptions.pdf_options.enable_layered_rendering = True
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_pdf_with_layered_rendering()