from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions, PdfOptimizationOptions

def set_max_resolution():
    # Load document
    with Viewer("sample.docx") as viewer:
        viewOptions = PdfViewOptions("set_max_resolution/optimized_resolution.pdf")
        viewOptions.pdf_optimization_options = PdfOptimizationOptions()
        viewOptions.pdf_optimization_options.compress_images = True
        viewOptions.pdf_optimization_options.image_quality = 50
        viewOptions.pdf_optimization_options.resize_images = True
        viewOptions.pdf_optimization_options.max_resolution = 100

        viewer.view(viewOptions)

if __name__ == "__main__":
    set_max_resolution()