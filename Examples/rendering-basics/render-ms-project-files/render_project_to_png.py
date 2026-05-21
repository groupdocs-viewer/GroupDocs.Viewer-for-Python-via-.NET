from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PngViewOptions

def render_project_to_png():
    import sys
    if sys.platform != "win32":
        print("Skipping: MS Project files (MPP/MPT/MPX) render on Windows only "
              "(GroupDocs.Viewer.CrossPlatform on Linux/macOS does not support Project).")
        return
    # Load Project file
    with Viewer("sample.mpp") as viewer:
        # Render the project's active view as PNG.
        # {0} is replaced with the current page number in the output file names.
        viewOptions = PngViewOptions("render_project_to_png/project_page_0_{0}.png")
        # Set width and height.
        viewOptions.width = 1600
        viewOptions.height = 650
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_project_to_png()