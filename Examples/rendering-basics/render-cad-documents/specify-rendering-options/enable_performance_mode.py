from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions, CadOptions

def enable_performance_mode():
    # Load CAD file
    with Viewer("input.dwg") as viewer:
        viewOptions = HtmlViewOptions.for_embedded_resources("enable_performance_mode/Output-Page#{0}.html")
        viewOptions.cad_options = CadOptions.for_rendering_by_width(1000)
        viewOptions.cad_options.enable_performance_conversion_mode = True

        viewer.view(viewOptions)

if __name__ == "__main__":
    enable_performance_mode()