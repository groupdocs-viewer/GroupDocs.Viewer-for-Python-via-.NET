from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_project_to_html():
    import sys
    if sys.platform != "win32":
        print("Skipping: MS Project files (MPP/MPT/MPX) render on Windows only "
              "(GroupDocs.Viewer.CrossPlatform on Linux/macOS does not support Project).")
        return
    # Load Project file
    with Viewer("sample.mpp") as viewer:
        # Render the project's active view as HTML.
        # {0} is replaced with the current page number in the output file names.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_project_to_html/pdf_page_{0}.html")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_project_to_html()