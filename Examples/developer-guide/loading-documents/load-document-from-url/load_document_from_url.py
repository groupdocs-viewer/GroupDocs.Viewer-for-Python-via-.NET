import requests
import io
from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def download_file(url):
    response = requests.get(url, stream=True, timeout=10)
    response.raise_for_status()
    return io.BytesIO(response.content)

def load_document_from_url():
    url = "https://github.com/groupdocs-viewer/GroupDocs.Viewer-for-.NET/blob/master/Examples/GroupDocs.Viewer.Examples.CSharp/Resources/SampleFiles/sample.docx?raw=true"

    stream = download_file(url)

    with Viewer(stream) as viewer:
        options = HtmlViewOptions.for_embedded_resources("load_document_from_url/page_{0}.html")
        viewer.view(options)

if __name__ == "__main__":
    load_document_from_url()