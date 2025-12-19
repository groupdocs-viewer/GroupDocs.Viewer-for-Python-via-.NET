from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_hidden_rows_and_columns():
    # Load spreadsheet
    with Viewer("invoice.xlsx") as viewer:
        # Convert the spreadsheet to PDF.
        viewOptions = PdfViewOptions("render_hidden_rows_and_columns/hidden_rows_and_columns.pdf")
        # Enable rendering hidden rows and columns.
        viewOptions.spreadsheet_options.render_hidden_columns = True
        viewOptions.spreadsheet_options.render_hidden_rows = True
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_hidden_rows_and_columns()