from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_xml_to_pdf():
    # Create PDF view options and specify output file path
    pdf_options = PdfViewOptions("render_xml_to_pdf/xml_document.pdf")
    
    # Load XML document
    with Viewer("sample.xml") as viewer:
        # Render XML document to PDF format
        # If content is large, it will be automatically paginated
        viewer.view(pdf_options)

if __name__ == "__main__":
    render_xml_to_pdf()