from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_ebook_to_pdf():
    # Load EBook
    with Viewer("sample.epub") as viewer:
        # Create a PDF file for the document.
        # Specify the PDF file name.
        viewOptions = PdfViewOptions("render_ebook_to_pdf/ebook.pdf")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_ebook_to_pdf()