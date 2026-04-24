from groupdocs.viewer import Viewer
from groupdocs.viewer.options import ViewInfoOptions

def get_file_type_and_pages_count():
    # Load PDF document
    with Viewer("sample.pdf") as viewer:
        info = viewer.get_view_info(ViewInfoOptions.for_html_view())

        print("Document type:", info.file_type)
        print("Pages count:", len(info.pages))

if __name__ == "__main__":
    get_file_type_and_pages_count()