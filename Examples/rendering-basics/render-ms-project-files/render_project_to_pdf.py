from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_project_to_pdf():
    import sys
    if sys.platform != "win32":
        print("Skipping: MS Project files (MPP/MPT/MPX) render on Windows only "
              "(GroupDocs.Viewer.CrossPlatform on Linux/macOS does not support Project).")
        return
    # Load Project file
    with Viewer("sample.mpp") as viewer:
        # Create a PDF file for the project's active view.
        viewOptions = PdfViewOptions("render_project_to_pdf/project_file.pdf")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_project_to_pdf()