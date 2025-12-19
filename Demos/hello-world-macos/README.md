# How to Run GroupDocs.Viewer for Python via .NET on macOS

## 1. Check if Requirements Are Met

Before installing and running the [groupdocs-viewer-net](https://pypi.org/project/groupdocs-viewer-net/) package on macOS, ensure that your system meets the following requirements:

* **Python**: Version **3.5–3.13** (inclusive)
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
groupdocs-viewer-net==25.12
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
```

## 7. Copy `sample.docx` to the Current Directory

Make sure `sample.docx` is located in the same directory as `render_docx_to_html.py`.

## 8. Run the Application

Run the script:

```bash
python render_docx_to_html.py
```

As a result, one or more HTML files (one per page) will be generated in the current directory.

## 9. Deactivate the Virtual Environment

When finished, deactivate the virtual environment:

```bash
deactivate
```

Alternatively, you can simply close the terminal.
