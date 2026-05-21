from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions, PageSize

def render_project_with_page_size():
    import sys
    if sys.platform != "win32":
        print("Skipping: MS Project files (MPP/MPT/MPX) render on Windows only "
              "(GroupDocs.Viewer.CrossPlatform on Linux/macOS does not support Project).")
        return
    # Load Project file
    with Viewer("sample.mpp") as viewer:
        # Convert the document to PDF.
        viewOptions = PdfViewOptions("render_project_with_page_size/project_with_page_size.pdf")
        # Specify the page size.
        viewOptions.project_management_options.page_size = PageSize.A3
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_project_with_page_size()