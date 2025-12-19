from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions, PdfOptimizationOptions

def optimize_pdf_for_web():
    # Load document
    with Viewer("sample.docx") as viewer:
        viewOptions = PdfViewOptions("optimize_pdf_for_web/optimized_spreadsheet.pdf")
        viewOptions.pdf_optimization_options = PdfOptimizationOptions()
        viewOptions.pdf_optimization_options.lineriaze = True

        viewer.view(viewOptions)

if __name__ == "__main__":
    optimize_pdf_for_web()