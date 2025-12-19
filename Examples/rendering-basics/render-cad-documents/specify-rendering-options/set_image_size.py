from groupdocs.viewer import Viewer
from groupdocs.viewer.options import PngViewOptions, CadOptions

def set_image_size():
    # Load CAD file
    with Viewer("sample.dwg") as viewer:
        # Convert the diagram to PNG.
        png_options = PngViewOptions("set_image_size/image_with_size_limits.pdf")
        # Specify a scale factor.
        png_options.cad_options = CadOptions.for_rendering_by_scale_factor(0.5)      
        viewer.view(png_options)

if __name__ == "__main__":
    set_image_size()