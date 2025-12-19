from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PdfViewOptions

def apply_pc3_file():
    # Load CAD file
    with Viewer("sample.dwg") as viewer:
        # Convert the diagram to PDF.
        viewOptions = PdfViewOptions("apply_pc3_file/apply_pc3_file.pdf")
        # Specify a path to the PC3 file.
        viewOptions.cad_options.pc_3_file = "small_page.pc3"
        viewer.view(viewOptions)

if __name__ == "__main__":
    apply_pc3_file()