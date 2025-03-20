from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_docx():
     with Viewer("sample.docx") as viewer:
        options = HtmlViewOptions.for_embedded_resources("page_{0}.html")
        viewer.view(options)

if __name__ == "__main__":
    render_docx()