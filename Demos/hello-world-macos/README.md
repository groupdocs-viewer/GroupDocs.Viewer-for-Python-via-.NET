# How to Run GroupDocs.Viewer for Python via .NET on macOS

## 1. Check if Requirements Are Met

Before installing and running the [groupdocs-viewer-net](https://pypi.org/project/groupdocs-viewer-net/) package on macOS, ensure that your system meets the following requirements:

* **Python**: Version **3.5–3.14** (inclusive)
* **libgdiplus**: Install via Homebrew:

  ```bash
  brew install mono-libgdiplus
  ```

> **Note**: If Homebrew is not installed, install it first from [https://brew.sh](https://brew.sh).

## 2. Create a Virtual Environment

Create a virtual environment in the current directory:

```bash
python3 -m venv .venv
```

## 3. Activate the Virtual Environment

Activate the virtual environment:

```bash
source .venv/bin/activate
```

## 4. Create a `requirements.txt` File

Create a `requirements.txt` file with the following content:

```text
groupdocs-viewer-net==26.4.0
```

## 5. Install Dependencies

Install the required Python package:

```bash
python -m pip install -r requirements.txt
```

## 6. Create the `render_docx_to_html.py` File

Create a file named `render_docx_to_html.py` with the following content:

```python
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
```

## 7. Copy `sample.docx` to the Current Directory

Make sure `sample.docx` is located in the same directory as `render_docx_to_html.py`.

## 8. Run the Application

Run the script:

```bash
python render_docx_to_html.py
```

As a result, HTML files (one per page) will be generated under an `output/` directory as `page_1.html`, `page_2.html`, …

> **Evaluation mode**: without a license, the output carries an **Aspose evaluation watermark** and is capped at a small number of pages. To render the full document, supply a valid license file — see the [Licensing and Subscription](https://docs.groupdocs.com/viewer/python-net/getting-started/licensing-and-subscription/) documentation page.

## 9. Deactivate the Virtual Environment

When finished, deactivate the virtual environment:

```bash
deactivate
```

Alternatively, you can simply close the terminal.
