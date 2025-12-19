from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions, PdfOptimizationOptions

def optimize_spreadsheets():
    # Load spreadsheet
    with Viewer("invoice.xlsx") as viewer:
        viewOptions = PdfViewOptions("optimize_spreadsheets/optimized_spreadsheet.pdf")
        viewOptions.pdf_optimization_options = PdfOptimizationOptions()
        viewOptions.pdf_optimization_options.optimize_spreadsheets = True

        viewer.view(viewOptions)

if __name__ == "__main__":
    optimize_spreadsheets()