import os
from groupdocs.viewer import License, Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_docx_to_html():
    # Get license file absolute path
    license_path = os.path.abspath("./GroupDocs.Viewer.lic")

    if os.path.exists(license_path):
        # Create License and set the path
        license = License()
        license.set_license(license_path)

    # Load DOCX file
    with Viewer("./sample.docx") as viewer:
        # Create view options
        html_options = HtmlViewOptions.for_embedded_resources("render_docx_to_html/page_{0}.html")

        # Render DOCX to HTML
        viewer.view(html_options)

if __name__ == "__main__":
    render_docx_to_html()