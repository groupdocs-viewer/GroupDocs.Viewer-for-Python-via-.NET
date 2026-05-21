from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions, TimeUnit

def render_project_with_time_unit():
    import sys
    if sys.platform != "win32":
        print("Skipping: MS Project files (MPP/MPT/MPX) render on Windows only "
              "(GroupDocs.Viewer.CrossPlatform on Linux/macOS does not support Project).")
        return
    # Load Project file
    with Viewer("sample.mpp") as viewer:
        # Convert the document to HTML.
        # {0} is replaced with the current page number in the file name.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_project_with_time_unit/output_{0}.html")
        # Specify the time unit.
        viewOptions.project_management_options.time_unit = TimeUnit.THIRDS_OF_MONTHS
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_project_with_time_unit()