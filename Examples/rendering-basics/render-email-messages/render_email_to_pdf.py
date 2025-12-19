from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_email_to_pdf():
    # Load email message
    with Viewer("sample.eml") as viewer:
        # Create a PDF file.
        viewOptions = PdfViewOptions("render_email_to_pdf/email_message.pdf")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_email_to_pdf()