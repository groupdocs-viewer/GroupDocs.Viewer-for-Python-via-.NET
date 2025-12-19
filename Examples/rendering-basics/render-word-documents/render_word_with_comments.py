from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_word_with_comments():
    # Load Word document
    with Viewer("with_comment.docx") as viewer:
        # Convert the document to PDF.
        viewOptions = PdfViewOptions("render_word_with_comments/word_with_comments.pdf")
        # Enable rendering comments.
        viewOptions.render_comments = True
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_word_with_comments()