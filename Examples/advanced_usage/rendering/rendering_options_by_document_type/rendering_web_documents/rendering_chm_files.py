# rendering_chm_files.py
# This example demonstrates how to render CHM document into HTML, JPG, PNG, PDF.

import os
import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = os.path.join(output_directory, "chm_result_{0}.html")

    # TO HTML
    with gv.Viewer(test_files.sample_chm) as viewer:
        html_options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        html_options.render_to_single_page = True  # Enable it if you want to convert all CHM content to a single page

        viewer.view(html_options, [1, 2, 3])  # Convert only 1, 2, 3 pages
        # viewer.view(html_options)  # Convert all pages

    # TO JPG
    page_file_path_format = os.path.join(output_directory, "chm_result_{0}.jpg")

    with gv.Viewer(test_files.sample_chm) as viewer:
        jpg_options = gvo.JpgViewOptions(page_file_path_format)

        viewer.view(jpg_options, [1, 2, 3])  # Convert only 1, 2, 3 pages
        # viewer.view(jpg_options)  # Convert all pages

    # TO PNG
    page_file_path_format = os.path.join(output_directory, "chm_result_{0}.png")

    with gv.Viewer(test_files.sample_chm) as viewer:
        png_options = gvo.PngViewOptions(page_file_path_format)

        viewer.view(png_options, [1, 2, 3])  # Convert only 1, 2, 3 pages
        # viewer.view(png_options)  # Convert all pages

    # TO PDF
    page_file_path_format = os.path.join(output_directory, "chm_result.pdf")

    with gv.Viewer(test_files.sample_chm) as viewer:
        pdf_options = gvo.PdfViewOptions(page_file_path_format)

        viewer.view(pdf_options)  # Convert all pages

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
