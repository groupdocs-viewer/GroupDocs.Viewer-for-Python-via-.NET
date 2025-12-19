from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def render_grid_lines():
    # Load spreadsheet
    with Viewer("invoice.xlsx") as viewer:
        # Convert the spreadsheet to PDF.
        viewOptions = PdfViewOptions("render_grid_lines/grid_lines.pdf")
        # Render grid lines.
        viewOptions.spreadsheet_options.render_grid_lines = True
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_grid_lines()