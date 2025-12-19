from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions, PdfOptimizationOptions

def convert_to_grayscale():
    # Load document
    with Viewer("sample.docx") as viewer:
        viewOptions = PdfViewOptions("convert_to_grayscale/grayscale_output.pdf")
        viewOptions.pdf_optimization_options = PdfOptimizationOptions()
        viewOptions.pdf_optimization_options.convert_to_gray_scale = True

        viewer.view(viewOptions)

if __name__ == "__main__":
    convert_to_grayscale()