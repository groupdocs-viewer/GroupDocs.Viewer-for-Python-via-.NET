from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_word_with_margins():
    # Load Word document
    with Viewer("sample.docx") as viewer:
        # Create an HTML file for each document page.
        # {0} is replaced with the current page number in the file name.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_word_with_margins/word_with_margins_{0}.html")
        # Specify the size of page margins in points.
        viewOptions.word_processing_options.left_margin = 54.0
        viewOptions.word_processing_options.right_margin = 54.0
        viewOptions.word_processing_options.top_margin = 72.0
        viewOptions.word_processing_options.bottom_margin = 72.0
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_word_with_margins()