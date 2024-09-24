# rendering_txt.py
# This example demonstrates how to render TXT document into HTML, JPG, PNG, PDF.

import os
import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_full_path = os.path.join(output_directory, "Txt_result.html")

    # TO MULTI PAGES HTML
    with gv.Viewer(test_files.sample_txt) as viewer:
        html_options = gvo.HtmlViewOptions.for_embedded_resources(page_file_full_path)

        viewer.view(html_options)

    page_file_full_path = os.path.join(output_directory, "Txt_result_single_page.html")

    # TO SINGLE HTML
    with gv.Viewer(test_files.sample_2_txt) as viewer:
        html_options = gvo.HtmlViewOptions.for_embedded_resources(page_file_full_path)
        html_options.render_to_single_page = True

        viewer.view(html_options)

    page_file_full_path = os.path.join(output_directory, "Txt_result.jpg")

    # TO JPG
    with gv.Viewer(test_files.sample_txt) as viewer:
        jpg_options = gvo.JpgViewOptions(page_file_full_path)

        viewer.view(jpg_options)

    page_file_full_path = os.path.join(output_directory, "Txt_result.png")

    # TO PNG
    with gv.Viewer(test_files.sample_txt) as viewer:
        png_options = gvo.PngViewOptions(page_file_full_path)

        viewer.view(png_options)

    page_file_full_path = os.path.join(output_directory, "Txt_result.pdf")

    # TO PDF
    with gv.Viewer(test_files.sample_txt) as viewer:
        pdf_options = gvo.PdfViewOptions(page_file_full_path)

        viewer.view(pdf_options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
