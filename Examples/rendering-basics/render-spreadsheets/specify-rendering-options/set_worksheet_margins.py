from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def set_worksheet_margins():

    # Load spreadsheet
    with Viewer("invoice.xlsx") as viewer:
        viewOptions = PdfViewOptions("set_worksheet_margins/worksheet_margins.pdf")

        # Set margins for worksheets in the output pdf pages
        viewOptions.spreadsheet_options.left_margin = 0.0
        viewOptions.spreadsheet_options.right_margin = 0.5
        viewOptions.spreadsheet_options.top_margin = 1.0
        viewOptions.spreadsheet_options.bottom_margin = -10.0
        viewer.view(viewOptions)

if __name__ == "__main__":
    set_worksheet_margins()