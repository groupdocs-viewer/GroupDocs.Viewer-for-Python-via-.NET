from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions, PdfOptimizationOptions

def subset_fonts():
    # Load document
    with Viewer("sample.docx") as viewer:
        viewOptions = PdfViewOptions("subset_fonts/subset_fonts.pdf")
        viewOptions.pdf_optimization_options = PdfOptimizationOptions()
        viewOptions.pdf_optimization_options.subset_fonts = True

        viewer.view(viewOptions)

if __name__ == "__main__":
    subset_fonts()