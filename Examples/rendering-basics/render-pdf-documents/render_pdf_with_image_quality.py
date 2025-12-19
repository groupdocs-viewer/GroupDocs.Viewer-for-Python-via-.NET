from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions, ImageQuality

def render_pdf_with_image_quality():
    # Load PDF document
    with Viewer("sample.pdf") as viewer:
        # Create an HTML files.
        # {0} is replaced with the current page number in the file name.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_pdf_with_image_quality/pdf_with_image_quality_{0}.html")
        # Set image quality to medium.
        viewOptions.pdf_options.image_quality = ImageQuality.MEDIUM 
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_pdf_with_image_quality()