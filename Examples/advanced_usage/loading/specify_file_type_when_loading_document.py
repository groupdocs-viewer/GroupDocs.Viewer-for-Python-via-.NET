# specify_file_type_when_loading_document.py
# This example demonstrates how to specify the file type when loading a document.

import os
import aspose.groupdocsviewer as gv
import aspose.groupdocsviewer.options as gvo
import test_files
import utils

def run():    
    output_directory = utils.get_output_directory_path()
    page_file_path_format = os.path.join(output_directory, "page_{0}.html")

    load_options = gvo.LoadOptions()
    load_options.file_type = gv.FileType.DOCX

    with gv.Viewer(test_files.sample_docx, load_options) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        viewer.view(options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
