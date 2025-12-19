from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions, PdfOptimizationOptions

def reduce_image_quality():
    # Load document
    with Viewer("sample.docx") as viewer:
        viewOptions = PdfViewOptions("reduce_image_quality/reduced_quality.pdf")
        viewOptions.pdf_optimization_options = PdfOptimizationOptions()
        viewOptions.pdf_optimization_options.compress_images = True
        viewOptions.pdf_optimization_options.image_quality = 50

        viewer.view(viewOptions)

if __name__ == "__main__":
    reduce_image_quality()