import os
from groupdocs.viewer import License, Viewer
from groupdocs.viewer.options import PngViewOptions

def render_docx_to_png():
    # Get license file absolute path
    license_path = os.path.abspath("./GroupDocs.Viewer.lic")

    if os.path.exists(license_path):
        # Create License and set the path
        license = License()
        license.set_license(license_path)

    # Load DOCX file
    with Viewer("./sample.docx") as viewer:
        # Create view options
        png_options = PngViewOptions("render_docx_to_png/output_{0}.png")

        # Render DOCX to PNG images
        viewer.view(png_options)

if __name__ == "__main__":
    render_docx_to_png()