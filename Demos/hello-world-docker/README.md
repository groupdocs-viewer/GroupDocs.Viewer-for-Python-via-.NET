# How to Run GroupDocs.Viewer for Python via .NET with Docker

This demo shows how to run [groupdocs-viewer-net](https://pypi.org/project/groupdocs-viewer-net/) in a Docker container, which handles all system dependencies automatically.

## Prerequisites

* **Docker**: Docker must be installed on your system. Download from [https://www.docker.com/get-started](https://www.docker.com/get-started)

## Project Structure

The project includes:
* `Dockerfile` - Container configuration with all dependencies
* `requirements.txt` - Python package dependencies
* `render_docx_to_html.py` - Main application script
* `sample.docx` - Sample document to convert

## 1. Build the Docker Image

Build the Docker image from the Dockerfile:

```bash
docker build -f Dockerfile -t groupdocs-viewer-for-python-via-net:hello-world-docker .
```

This will:
* Use Python 3.11 slim base image
* Install Microsoft Fonts for proper rendering
* Install System.Drawing.Common dependencies (libgdiplus, libc6-dev)
* Install globalization and cryptography dependencies (libicu67, libssl1.1)
* Install the `groupdocs-viewer-net` package

## 2. Run the Docker Container

Run the container with a volume mount to access the output files:

**On Linux/macOS:**
```bash
docker run --rm -v "${PWD}/output:/output" groupdocs-viewer-for-python-via-net:hello-world-docker
```

**On Windows PowerShell:**
```powershell
docker run --rm -v "${PWD}/output:/output" groupdocs-viewer-for-python-via-net:hello-world-docker
```

**On Windows Command Prompt:**
```cmd
docker run --rm -v "%CD%/output:/output" groupdocs-viewer-for-python-via-net:hello-world-docker
```

The `--rm` flag automatically removes the container after it exits, and the `-v` flag mounts the local `output` directory to `/output` inside the container.

## 3. View the Results

After the container runs, check the `output` directory. You should find one or more HTML files (one per page) named `page_0.html`, `page_1.html`, etc.

## How It Works

The Docker container:
1. Loads the `sample.docx` file from the container's working directory
2. Converts it to HTML using GroupDocs.Viewer
3. Saves the output files to `/output` inside the container
4. The volume mount makes these files accessible in your local `output` directory

