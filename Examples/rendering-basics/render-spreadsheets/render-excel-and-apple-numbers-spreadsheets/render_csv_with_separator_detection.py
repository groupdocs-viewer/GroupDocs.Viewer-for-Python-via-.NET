from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_csv_with_separator_detection():
    # Load CSV file
    with Viewer("sample.csv") as viewer:
        # Convert the spreadsheet to HTML.
        # {0} is replaced with the current page number in the file names.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_csv_with_separator_detection/csv_with_separator_detection_{0}.html")
        # Detect a CSV/TSV separator.
        viewOptions.spreadsheet_options.detect_separator = True
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_csv_with_separator_detection()