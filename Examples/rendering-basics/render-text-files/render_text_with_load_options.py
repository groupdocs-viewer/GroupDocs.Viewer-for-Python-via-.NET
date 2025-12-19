from groupdocs.viewer import Viewer, FileType
from groupdocs.viewer.options import LoadOptions, PdfViewOptions

def render_text_with_load_options():
    # Specify the file encoding. 
    load_options = LoadOptions(FileType.MD)
    # Convert the document to PDF.
    with Viewer("terms_of_service.txt", load_options) as viewer:
        viewOptions = PdfViewOptions("render_text_with_load_options/text_with_load_options.pdf")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_text_with_load_options()