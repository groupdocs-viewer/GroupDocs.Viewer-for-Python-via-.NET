# load_document_from_stream.py
# This example demonstrates how to render a document from a stream.

import os
import aspose.groupdocsviewer as gv
import aspose.groupdocsviewer.options as gvo
import test_files
import utils

def run():    
    output_directory = utils.get_output_directory_path()
    page_file_path_format = os.path.join(output_directory, "page_{0}.html")
    stream = get_file_stream()
    
    with gv.Viewer(stream) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        viewer.view(options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

def get_file_stream():
    file_path = test_files.sample_docx
    return open(file_path, "rb")

if __name__ == "__main__":
    run()
