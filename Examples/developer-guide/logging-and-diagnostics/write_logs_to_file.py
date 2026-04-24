from groupdocs.viewer import Viewer, ViewerSettings
from groupdocs.viewer.logging import FileLogger
from groupdocs.viewer.options import HtmlViewOptions

def write_logs_to_file():
    # Create a file logger that writes trace/warning/error messages to log.txt
    # and wire it through ViewerSettings
    viewer_settings = ViewerSettings(logger=FileLogger("./log.txt"))

    # Load DOCX document and render it to HTML
    with Viewer("./sample.docx", settings=viewer_settings) as viewer:
        html_options = HtmlViewOptions.for_embedded_resources("write_logs_to_file/page_{0}.html")
        viewer.view(html_options)

if __name__ == "__main__":
    write_logs_to_file()