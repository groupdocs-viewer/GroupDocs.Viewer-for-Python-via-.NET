from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def reorder_pages():
    # Load document
    with Viewer("sample.docx") as viewer:
        # Create view options.
        viewOptions = PdfViewOptions("reorder_pages/reordered_pages.pdf")

        # Pass page numbers in the order you want to render them.
        viewer.view(viewOptions, [2, 1])

if __name__ == "__main__":
    reorder_pages()