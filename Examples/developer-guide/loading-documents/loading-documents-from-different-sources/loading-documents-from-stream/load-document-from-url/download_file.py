import requests
import io
from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def download_file(url):
    response = requests.get(url, stream=True, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:25.0) Gecko/20100101 Firefox/25.0"}, timeout=10)
    # Check if the request was successful (status code 200)
    response.raise_for_status()
    # Create a BytesIO stream from the content
    stream = io.BytesIO(response.content)
    return stream

def load_document_from_url():

    url = "https://github.com/groupdocs-viewer/GroupDocs.Viewer-for-.NET/blob/master/Examples/GroupDocs.Viewer.Examples.CSharp/Resources/SampleFiles/sample.docx?raw=true"
    
    stream = download_file(url)

    with Viewer(stream) as viewer:
        options = HtmlViewOptions.for_embedded_resources("load_document_from_url/download_file_{0}.html")
        viewer.view(options)

if __name__ == "__main__":
    load_document_from_url()