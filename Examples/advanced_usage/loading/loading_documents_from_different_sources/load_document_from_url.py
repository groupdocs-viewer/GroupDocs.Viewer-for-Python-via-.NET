# load_document_from_url.py
# This example demonstrates how to download and render a document from a URL.

import os
import requests
import io
import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import test_files
import utils

def run():    
    output_directory = utils.get_output_directory_path()
    url = "https://cms.admin.containerize.com/templates/groupdocs/images/logos/groupdocs-logo.png"    
    page_file_path_format = os.path.join(output_directory, "page_{0}.html")

    stream = download_file(url)

    with gv.Viewer(stream) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        viewer.view(options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

def download_file(url):
    response = requests.get(url, stream=True, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:25.0) Gecko/20100101 Firefox/25.0"}, timeout=10)
         
    # Check if the request was successful (status code 200)
    response.raise_for_status()
    
    # Create a BytesIO stream from the content
    stream = io.BytesIO(response.content)
    
    return stream

if __name__ == "__main__":
    run()
