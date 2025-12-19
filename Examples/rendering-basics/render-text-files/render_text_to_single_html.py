from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_text_to_single_html():
    # Load text file
    with Viewer("terms_of_service.txt") as viewer:
        # Create an HTML file.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_text_to_single_html/text_to_single_html.html")
        # Render the file to a single page. 
        viewOptions.render_to_single_page = True
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_text_to_single_html()