from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_archive_to_pdf():
    # Load archive file
    with Viewer("documents.zip") as viewer:
        # Create a PDF file.
        viewOptions = PdfViewOptions("render_archive_to_pdf/archive_content.pdf")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_archive_to_pdf()