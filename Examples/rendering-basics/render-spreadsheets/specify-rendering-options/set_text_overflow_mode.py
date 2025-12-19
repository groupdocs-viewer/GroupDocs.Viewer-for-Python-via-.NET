from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions, TextOverflowMode

def set_text_overflow_mode():
    # Load spreadsheet
    with Viewer("invoice.xlsx") as viewer:
        # Convert the spreadsheet to PDF.
        viewOptions = PdfViewOptions("set_text_overflow_mode/text_overflow_mode.pdf")
        # Specify the AUTO_FIT_COLUMN mode.
        viewOptions.spreadsheet_options.text_overflow_mode = TextOverflowMode.AUTO_FIT_COLUMN 
        viewer.view(viewOptions)

if __name__ == "__main__":
    set_text_overflow_mode()