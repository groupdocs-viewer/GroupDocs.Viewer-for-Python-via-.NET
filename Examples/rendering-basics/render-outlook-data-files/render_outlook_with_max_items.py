from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_outlook_with_max_items():
    # Load Outlook data file
    with Viewer("sample.pst") as viewer:
        # Create an HTML file.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_outlook_with_max_items/outlook_with_max_items.html")
        # Specify the maximum number of folder items.
        viewOptions.outlook_options.max_items_in_folder = 30
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_outlook_with_max_items()