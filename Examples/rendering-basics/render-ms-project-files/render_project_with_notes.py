from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_project_with_notes():
    # Load Project file
    with Viewer("sample.mpp") as viewer:
        # Convert the document to PDF.
        viewOptions = PdfViewOptions("render_project_with_notes/project_with_notes.pdf")
        # Enable notes rendering.
        viewOptions.render_notes = True
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_project_with_notes()