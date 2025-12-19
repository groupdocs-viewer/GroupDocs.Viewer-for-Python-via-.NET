from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_project_to_pdf():
    # Load Project file
    with Viewer("sample.mpp") as viewer:
        # Create a PDF file for the project's active view.
        viewOptions = PdfViewOptions("render_project_to_pdf/project_file.pdf")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_project_to_pdf()