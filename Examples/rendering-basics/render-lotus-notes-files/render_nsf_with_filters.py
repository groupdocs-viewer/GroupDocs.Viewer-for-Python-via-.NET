from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_nsf_with_filters():
    # Load NSF file
    with Viewer("sample.nsf") as viewer:
        # Create an HTML file.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_nsf_with_filters/nsf_with_filters.html")
        # Set filters
        viewOptions.mail_storage_options.text_filter = "Viewer"
        viewOptions.mail_storage_options.address_filter = "groupdocs@mail.com"
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_nsf_with_filters()