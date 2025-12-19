from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PngViewOptions, JpgViewOptions

def render_xml_to_images():
    # Create PNG view options
    # {0} will be replaced with page number if content spans multiple images
    pngOptions = PngViewOptions("render_xml_to_images/page-{0}.png")
    
    # Create JPEG view options
    jpegOptions = JpgViewOptions("render_xml_to_images/page-{0}.jpeg")
    # Set JPEG image quality (1-100, default is 90)
    jpegOptions.quality = 80

    # Load XML document
    with Viewer("sample.xml") as viewer:
        # Render XML document to PNG format
        viewer.view(pngOptions)
        # Render XML document to JPEG format
        viewer.view(jpegOptions)

if __name__ == "__main__":
    render_xml_to_images()