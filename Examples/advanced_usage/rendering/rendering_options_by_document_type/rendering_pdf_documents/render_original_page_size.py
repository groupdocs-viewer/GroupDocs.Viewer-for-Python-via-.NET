# render_original_page_size.py
# This example demonstrates how to render pages to PNG and set page size to be the same as size of pages in a source document.

import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import os
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = os.path.join(output_directory, "page_{0}.png")

    with gv.Viewer(test_files.sample_pdf) as viewer:
        options = gvo.PngViewOptions(page_file_path_format)
        options.pdf_options.render_original_page_size = True
        viewer.view(options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
