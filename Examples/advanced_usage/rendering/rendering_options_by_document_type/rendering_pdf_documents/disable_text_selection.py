# disable_text_selection.py
# This example demonstrates how to disable text selection when rendering PDF documents to HTML.

import os
from os.path import join
import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = join(output_directory, "page_{0}.html")

    with gv.Viewer(test_files.one_page_text_pdf) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        options.pdf_options.render_text_as_image = True

        viewer.view(options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
