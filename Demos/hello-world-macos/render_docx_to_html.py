"""
Convert a DOCX document to HTML using GroupDocs.Viewer for Python via .NET.

Reads sample.docx from the working directory and writes one HTML page per
document page into output/ with embedded resources (CSS, fonts, images).

If a license is available via the GROUPDOCS_LIC_PATH environment variable or
as a .lic file next to the script, it is applied automatically. Otherwise the
render runs in evaluation mode — a small number of pages with a watermark.
"""

import glob
import os

from groupdocs.viewer import License, Viewer
from groupdocs.viewer.options import HtmlViewOptions


def apply_license_if_available():
    """Apply a GroupDocs license from GROUPDOCS_LIC_PATH or a local .lic file."""
    env_path = os.environ.get("GROUPDOCS_LIC_PATH")
    if env_path and os.path.isfile(env_path):
        License().set_license(env_path)
        return env_path

    # Fall back: any *.lic file next to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    for lic_path in glob.glob(os.path.join(script_dir, "*.lic")):
        License().set_license(lic_path)
        return lic_path

    return None


def render_docx_to_html():
    """Render sample.docx to output/page_{N}.html with embedded resources."""
    applied = apply_license_if_available()
    if applied:
        print(f"License applied from {applied}")
    else:
        print("Running in evaluation mode (no license found).")

    with Viewer("sample.docx") as viewer:
        # The {0} placeholder is replaced with the 1-based page number, so
        # this pattern generates output/page_1.html, output/page_2.html, ...
        options = HtmlViewOptions.for_embedded_resources("output/page_{0}.html")
        viewer.view(options)


if __name__ == "__main__":
    render_docx_to_html()
