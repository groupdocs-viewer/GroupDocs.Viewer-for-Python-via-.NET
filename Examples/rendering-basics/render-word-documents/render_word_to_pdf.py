from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_word_to_pdf():
    # Load Word document
    with Viewer("sample.docx") as viewer:
        # Create a PDF file for the document.
        # Specify the PDF file name.
        viewOptions = PdfViewOptions("render_word_to_pdf/word_document.pdf")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_word_to_pdf()