from groupdocs.viewer import Viewer
from groupdocs.viewer.options import ViewInfoOptions

def get_cad_info():
    # Load CAD file
    with Viewer("sample.dwg") as viewer:
        viewInfoOptions = ViewInfoOptions.for_html_view()
        cad_info = viewer.get_view_info(viewInfoOptions)
        # Display information about the CAD file.
        print("File type:", cad_info.file_type)
        print("Pages count:", len(cad_info.pages))

        print("\nView info retrieved successfully.")

if __name__ == "__main__":
    get_cad_info()