# How to Run GroupDocs.Viewer for Python via .NET on macOS

## 1. Check if Requirements Are Met  

Before installing and running the [groupdocs-viewer-net](https://pypi.org/project/groupdocs-viewer-net/) package on macOS, ensure that your system meets the following requirements:  

- **CPU**: ARM64 (Apple Silicon: M1, M2, etc.)  
- **Python**: Version **≥ 3.9** and **≤ 3.12**  
- **.NET Runtime**: [.NET 6.0](https://dotnet.microsoft.com/en-us/download/dotnet/6.0) or later for macOS  

## 2. Create a Virtual Environment  

Run the following command to create a virtual environment:  

```bash
python3 -m venv .venv
```

## 3. Activate the Virtual Environment  

Activate the virtual environment using:  

```bash
source .venv/bin/activate
```

## 4. Create a `requirements.txt` File  

Create a `requirements.txt` file with the following content:  

```bash
groupdocs-viewer-net==24.9
```

## 5. Install Dependencies  

Run the following command to install the required dependencies:  

```bash
python3 -m pip install -r requirements.txt
```

## 6. Create the `app.py` File  

Create a file named `app.py` and add the following content:  

```py
from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_docx():
    with Viewer("sample.docx") as viewer:
        options = HtmlViewOptions.for_embedded_resources("page_{0}.html")
        viewer.view(options)

if __name__ == "__main__":
    render_docx()
```

## 7. Copy `sample.docx` to the Current Directory  

Ensure that `sample.docx` is present in the same directory as `app.py`.  

## 8. Run the Application  

Execute the following command to run the script:  

```bash
python3 app.py
```

As a result, you will get two HTML files in the current directory.  

## 9. Deactivate the Virtual Environment (Optional)  

When finished, you can deactivate the virtual environment by running:  

```bash
deactivate
```

Alternatively, you can simply close the terminal.
