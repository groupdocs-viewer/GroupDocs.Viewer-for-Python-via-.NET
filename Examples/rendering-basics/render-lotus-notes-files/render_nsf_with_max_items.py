from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_nsf_with_max_items():
    # Load NSF file
    with Viewer("sample.nsf") as viewer:
        # Create an HTML file.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_nsf_with_max_items/nsf_with_max_items.html")
        # Specify the maximum items to render.
        viewOptions.mail_storage_options.max_items = 20
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_nsf_with_max_items()