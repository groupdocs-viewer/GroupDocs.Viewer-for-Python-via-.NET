from groupdocs.viewer import Viewer
from groupdocs.viewer.options import JpgViewOptions

def render_project_to_jpg():
    # Load Project file
    with Viewer("sample.mpp") as viewer:
        # Render the project's active view as JPEG.
        # {0} is replaced with the current page number in the output file names.
        viewOptions = JpgViewOptions("render_project_to_jpg/project_to_jpg_{0}.jpg")
        # Set width and height.
        viewOptions.width = 1600
        viewOptions.height = 650
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_project_to_jpg()