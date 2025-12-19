from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_xml_to_html():
    # Create HTML view options for paginated output
    # {0} will be replaced with page number
    paginated_html_options = HtmlViewOptions.for_embedded_resources("render_xml_to_html/page-{0}.html")
    
    # Create HTML view options for single-page output
    single_html_options = HtmlViewOptions.for_embedded_resources("render_xml_to_html/single-page.html")
    # Enable single-page rendering - all XML content in one HTML file
    single_html_options.render_to_single_page = True

    # Load XML document
    with Viewer("sample.xml") as viewer:
        # Render to paginated HTML (multiple HTML files)
        viewer.view(paginated_html_options)
        # Render to single-page HTML (one HTML file)
        viewer.view(single_html_options)

if __name__ == "__main__":
    render_xml_to_html()