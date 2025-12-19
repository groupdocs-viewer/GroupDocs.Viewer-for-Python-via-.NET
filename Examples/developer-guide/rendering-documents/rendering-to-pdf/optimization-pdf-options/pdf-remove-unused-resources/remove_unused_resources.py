from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions, PdfOptimizationOptions

def remove_unused_resources():

    view_options_1 = PdfViewOptions("remove_unused_resources/removed_unused_objects.pdf")
    view_options_1.pdf_optimization_options = PdfOptimizationOptions()
    view_options_1.pdf_optimization_options.remove_unused_objects = True

    view_options_2 = PdfViewOptions("remove_unused_resources/removed_unused_streams.pdf")
    view_options_2.pdf_optimization_options = PdfOptimizationOptions()
    view_options_2.pdf_optimization_options.remove_unused_streams = True

    with Viewer("sample.pdf") as viewer:
        viewer.view(view_options_1)
        viewer.view(view_options_2)

if __name__ == "__main__":
    remove_unused_resources()