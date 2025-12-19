from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions, PdfOptimizationOptions

def remove_form_fields():
    # Load document
    with Viewer("sample.docx") as viewer:
        viewOptions = PdfViewOptions("remove_form_fields/without_form_fields.pdf")
        viewOptions.pdf_optimization_options = PdfOptimizationOptions()
        viewOptions.pdf_optimization_options.remove_form_fields = True

        viewer.view(viewOptions)

if __name__ == "__main__":
    remove_form_fields()