from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions, PdfOptimizationOptions

def remove_annotations():
    # Load document
    with Viewer("sample.docx") as viewer:
        viewOptions = PdfViewOptions("remove_annotations/without_annotations.pdf")
        viewOptions.pdf_optimization_options = PdfOptimizationOptions()
        viewOptions.pdf_optimization_options.remove_annotations = True

        viewer.view(viewOptions)

if __name__ == "__main__":
    remove_annotations()