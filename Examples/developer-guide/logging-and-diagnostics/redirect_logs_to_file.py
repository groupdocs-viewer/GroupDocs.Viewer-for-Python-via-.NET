import sys
from groupdocs.viewer import Viewer, ViewerSettings
from groupdocs.viewer.logging import ConsoleLogger
from groupdocs.viewer.options import HtmlViewOptions

def redirect_logs_to_file():
    log_file_path = "./log.txt"

    # Redirect standard output to a file so ConsoleLogger writes into it
    original_stdout = sys.stdout
    with open(log_file_path, "w", encoding="utf-8") as log_file:
        sys.stdout = log_file
        try:
            # Create viewer settings with a console logger — the logger
            # writes through sys.stdout, which is currently redirected to log_file.
            viewer_settings = ViewerSettings(logger=ConsoleLogger())

            # Load DOCX document and render it to HTML
            with Viewer("./sample.docx", settings=viewer_settings) as viewer:
                html_options = HtmlViewOptions.for_embedded_resources("redirect_logs_to_file/page_{0}.html")
                viewer.view(html_options)
        finally:
            sys.stdout = original_stdout

if __name__ == "__main__":
    redirect_logs_to_file()