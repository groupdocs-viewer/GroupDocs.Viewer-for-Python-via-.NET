from groupdocs.viewer import Viewer, ViewerSettings
from groupdocs.viewer.logging import ConsoleLogger
from groupdocs.viewer.options import HtmlViewOptions

def write_logs_to_console():
    # Create viewer settings with a console logger
    viewer_settings = ViewerSettings(logger=ConsoleLogger())

    # Load DOCX document and render it to HTML
    with Viewer("./sample.docx", settings=viewer_settings) as viewer:
        html_options = HtmlViewOptions.for_embedded_resources("write_logs_to_console/page_{0}.html")
        viewer.view(html_options)

if __name__ == "__main__":
    write_logs_to_console()