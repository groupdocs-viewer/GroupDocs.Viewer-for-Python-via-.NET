from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions, PdfOptimizationOptions

def optimize_pdf_resources():
    # Load document
    with Viewer("sample.docx") as viewer:
        viewOptions = PdfViewOptions("optimize_pdf_resources/optimized_spreadsheet.pdf")
        viewOptions.pdf_optimization_options = PdfOptimizationOptions()

        viewer.view(viewOptions)

if __name__ == "__main__":
    optimize_pdf_resources()