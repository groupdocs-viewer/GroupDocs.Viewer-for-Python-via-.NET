from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions, ImageQuality

def render_pdf_text_as_image():
    # Load PDF document
    with Viewer("sample.pdf") as viewer:
        # Create an HTML files.
        # {0} is replaced with the current page number in the file name.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_pdf_text_as_image/text-as-image_{0}.html")
        # Enable rendering text as image.
        viewOptions.pdf_options.image_quality = ImageQuality.MEDIUM 
        viewOptions.pdf_options.render_text_as_image = True
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_pdf_text_as_image()