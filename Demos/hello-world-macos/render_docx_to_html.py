"""
Convert a DOCX document to HTML using GroupDocs.Viewer for Python via .NET.

This script reads a sample.docx file and generates HTML pages (one per page)
in the output directory with embedded resources.
"""

from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions


def render_docx_to_html():
    """
    Renders a DOCX document to HTML format.
    
    The function opens the sample.docx file, creates HTML view options
    with embedded resources, and generates HTML files in the output directory.
    Each page of the document will be saved as a separate HTML file.
    """
    # Open the DOCX file using Viewer context manager for automatic resource cleanup
    with Viewer("sample.docx") as viewer:
        # Configure HTML view options with embedded resources
        # The pattern "output/page_{0}.html" will generate files like:
        # output/page_0.html, output/page_1.html, etc.
        options = HtmlViewOptions.for_embedded_resources("output/page_{0}.html")
        
        # Render the document to HTML using the specified options
        viewer.view(options)


if __name__ == "__main__":
    # Execute the conversion when the script is run directly
    render_docx_to_html()