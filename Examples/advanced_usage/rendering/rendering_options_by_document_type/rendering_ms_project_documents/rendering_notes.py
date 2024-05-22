# rendering_notes.py
# This example demonstrates how to render MS Project document into HTML, JPG, PNG, PDF with notes.

import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import os
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = os.path.join(output_directory, "mpp_result.html")

    # TO HTML
    with gv.Viewer(test_files.sample_mpp) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        options.render_notes = True

        viewer.view(options)

    # TO JPG
    page_file_path_format = os.path.join(output_directory, "mpp_{0}_result.jpg")

    with gv.Viewer(test_files.sample_mpp) as viewer:
        options = gvo.JpgViewOptions(page_file_path_format)
        options.render_notes = True

        viewer.view(options)

    # TO PNG
    page_file_path_format = os.path.join(output_directory, "mpp_{0}_result.png")

    with gv.Viewer(test_files.sample_mpp) as viewer:
        options = gvo.PngViewOptions(page_file_path_format)
        options.render_notes = True

        viewer.view(options)

    # TO PDF
    page_file_path_format = os.path.join(output_directory, "mpp_result.pdf")

    with gv.Viewer(test_files.sample_mpp) as viewer:
        options = gvo.PdfViewOptions(page_file_path_format)
        options.render_notes = True

        viewer.view(options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
