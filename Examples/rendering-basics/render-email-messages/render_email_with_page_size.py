from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions, PageSize

def render_email_with_page_size():
    # Load email message
    with Viewer("sample.eml") as viewer:
        # Create a PDF file.
        viewOptions = PdfViewOptions("render_email_with_page_size/email_with_page_size.pdf")
        # Specify the page size.
        viewOptions.email_options.page_size = PageSize.LETTER
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_email_with_page_size()