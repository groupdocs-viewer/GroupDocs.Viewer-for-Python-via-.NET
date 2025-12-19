from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_word_with_tracked_changes():
    # Load Word document
    with Viewer("with_tracked_changes.docx") as viewer:
        # Convert the document to PDF.
        viewOptions = PdfViewOptions("render_word_with_tracked_changes/word_with_tracked_changes.pdf")
        # Enable tracked changes rendering.
        viewOptions.word_processing_options.render_tracked_changes = True
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_word_with_tracked_changes()