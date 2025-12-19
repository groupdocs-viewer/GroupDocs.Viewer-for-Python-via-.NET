from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_outlook_to_pdf():
    # Load Outlook data file
    with Viewer("sample.pst") as viewer:
        # Create a PDF file.
        viewOptions = PdfViewOptions("render_outlook_to_pdf/outlook_data.pdf")
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_outlook_to_pdf()