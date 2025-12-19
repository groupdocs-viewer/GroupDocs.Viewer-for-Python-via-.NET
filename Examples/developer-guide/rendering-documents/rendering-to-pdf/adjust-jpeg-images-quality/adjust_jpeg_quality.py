from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions, PdfOptimizationOptions

def adjust_jpeg_quality():
    # Load document
    with Viewer("sample.docx") as viewer:
        # Create view options.
        viewOptions = PdfViewOptions("adjust_jpeg_quality/optimized_jpeg_quality.pdf")

        # Specify the JPG image quality.
        pdf_optimization_options = PdfOptimizationOptions()
        pdf_optimization_options.image_quality = 50
        # Specify pdf_optimization_options object
        viewOptions.pdf_optimization_options = pdf_optimization_options

        viewer.view(viewOptions)

if __name__ == "__main__":
    adjust_jpeg_quality()