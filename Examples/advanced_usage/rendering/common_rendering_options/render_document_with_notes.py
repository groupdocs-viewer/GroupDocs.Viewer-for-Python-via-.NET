# render_document_with_notes.py
# This example demonstrates how to render a presentation with notes.

import os
import aspose.groupdocsviewer as gv
import aspose.groupdocsviewer.options as gvo
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = os.path.join(output_directory, "page_{0}.html")

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with gv.Viewer(test_files.pptx_with_notes) as viewer:
        html_options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        html_options.render_notes = True

        viewer.view(html_options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
