from groupdocs.viewer import Viewer
from groupdocs.viewer.options import ViewInfoOptions

def get_pdf_information():
    # Load PDF document
    with Viewer("sample.pdf") as viewer:
        viewInfoOptions = ViewInfoOptions.for_html_view()
        view_info = viewer.get_view_info(viewInfoOptions)
        # Display information about the PDF document.
        print("File type:", view_info.file_type)
        print("The number of pages:", len(view_info.pages))

if __name__ == "__main__":
    get_pdf_information()