# render_row_and_column_headings.py
# This example demonstrates how to render row and column headings.

import os
import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = os.path.join(output_directory, "page_{0}.html")

    with gv.Viewer(test_files.sample_xlsx) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        options.spreadsheet_options.render_headings = True

        viewer.view(options,  [1, 2, 3])

    # TO JPG
    page_file_path_format = os.path.join(output_directory, "page_{0}.jpg")

    with gv.Viewer(test_files.sample_xlsx) as viewer:
        options = gvo.JpgViewOptions(page_file_path_format)
        options.spreadsheet_options.render_headings = True

        viewer.view(options,  [1, 2, 3])

    # TO PNG
    page_file_path_format = os.path.join(output_directory, "page_{0}.png")

    with gv.Viewer(test_files.sample_xlsx) as viewer:
        options = gvo.PngViewOptions(page_file_path_format)
        options.spreadsheet_options.render_headings = True

        viewer.view(options,  [1, 2, 3])

    # TO PDF
    output_file_path = os.path.join(output_directory, "output.pdf")

    with gv.Viewer(test_files.sample_xlsx) as viewer:
        options = gvo.PdfViewOptions(output_file_path)
        options.spreadsheet_options.render_headings = True

        viewer.view(options,  [1, 2, 3])

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
