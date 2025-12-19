from groupdocs.viewer import Viewer
from groupdocs.viewer.options import ViewInfoOptions
from groupdocs.viewer.results import ProjectManagementViewInfo

def get_project_info():
    # Load Project file
    with Viewer("sample.mpp") as viewer:
        viewOptions = ViewInfoOptions.for_html_view()
        view_info = viewer.get_view_info(viewOptions)       
        print("File type: " + str(view_info.file_type))
        print("The number of pages: " + str(len(view_info.pages)))

if __name__ == "__main__":
    get_project_info()