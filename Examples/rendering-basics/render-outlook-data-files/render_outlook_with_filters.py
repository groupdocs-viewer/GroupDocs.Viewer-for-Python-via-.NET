from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_outlook_with_filters():
    # Load Outlook data file
    with Viewer("sample.pst") as viewer:
        # Create an HTML file.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_outlook_with_filters/outlook_with_filters.html")
        # Set filters.
        viewOptions.outlook_options.text_filter = "Viewer"
        viewOptions.outlook_options.address_filter = "groupdocs.com"
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_outlook_with_filters()