from typing import cast
from groupdocs.viewer import Viewer
from groupdocs.viewer.options import ViewInfoOptions
from groupdocs.viewer.results import PdfViewInfo

def get_file_type_and_pages_count():
    # Load PDF document
    with Viewer("sample.pdf") as viewer:
        options = ViewInfoOptions.for_html_view() 
        info = viewer.get_view_info(options)
        pdf_info = cast(PdfViewInfo, info)

        print("Document type is:", pdf_info.file_type)
        print("Pages count:", len(pdf_info.pages))

        print("\nView info retrieved successfully.")

if __name__ == "__main__":
    get_file_type_and_pages_count()