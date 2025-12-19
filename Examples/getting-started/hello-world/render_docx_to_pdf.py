import os
from groupdocs.viewer import License, Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_docx_to_pdf():
    # Get license file absolute path
    license_path = os.path.abspath("./GroupDocs.Viewer.lic")

    if os.path.exists(license_path):
        # Create License and set the path
        license = License()
        license.set_license(license_path)

    # Load DOCX file
    with Viewer("./sample.docx") as viewer:
        # Create view options
        pdf_options = PdfViewOptions("render_docx_to_pdf/output.pdf")

        # Render DOCX to PDF
        viewer.view(pdf_options)

if __name__ == "__main__":
    render_docx_to_pdf()