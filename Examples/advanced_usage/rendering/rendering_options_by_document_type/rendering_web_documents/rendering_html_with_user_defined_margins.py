# rendering_html_with_user_defined_margins.py
# This example demonstrates how to render HTML files with user-defined margins.

import os
import aspose.groupdocsviewer as gv
import aspose.groupdocsviewer.options as gvo
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = os.path.join(output_directory, "html_render_margins_page_{0}.jpg")

    # TO JPG
    with gv.Viewer(test_files.sample_html) as viewer:
        jpg_options = gvo.JpgViewOptions(page_file_path_format)
        jpg_options.word_processing_options.left_margin = 40.0
        jpg_options.word_processing_options.right_margin = 40.0
        jpg_options.word_processing_options.top_margin = 40.0
        jpg_options.word_processing_options.bottom_margin = 40.0

        viewer.view(jpg_options)

    page_file_path_format = os.path.join(output_directory, "html_render_margins_page_{0}.png")

    # TO PNG
    with gv.Viewer(test_files.sample_html) as viewer:
        png_options = gvo.PngViewOptions(page_file_path_format)
        png_options.word_processing_options.left_margin = 40.0
        png_options.word_processing_options.right_margin = 40.0
        png_options.word_processing_options.top_margin = 40.0
        png_options.word_processing_options.bottom_margin = 40.0

        viewer.view(png_options)

    page_file_path_format = os.path.join(output_directory, "html_render_margins.pdf")

    # TO PDF
    with gv.Viewer(test_files.sample_html) as viewer:
        pdf_options = gvo.PdfViewOptions(page_file_path_format)
        pdf_options.word_processing_options.left_margin = 40.0
        pdf_options.word_processing_options.right_margin = 40.0
        pdf_options.word_processing_options.top_margin = 40.0
        pdf_options.word_processing_options.bottom_margin = 40.0

        viewer.view(pdf_options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
