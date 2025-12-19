from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions, Security, Permissions

def protect_pdf_document():
    # Load document
    with Viewer("sample.docx") as viewer:
        # Specify the security settings.
        security = Security()
        security.document_open_password = "o123"
        security.permissions_password = "p123"
        security.permissions = Permissions.ALLOW_ALL & ~Permissions.DENY_PRINTING

        # Create a PDF file.
        pdf_options = PdfViewOptions("protect_pdf_document/protected_document.pdf")

        # Apply the security settings
        pdf_options.security = security
        viewer.view(pdf_options)

if __name__ == "__main__":
    protect_pdf_document()