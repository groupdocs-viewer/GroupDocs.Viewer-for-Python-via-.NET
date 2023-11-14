# rendering_visio_documents_figures.py
# This example demonstrates how to render Visio documents figures into HTML, JPG, PNG, PDF.

import os
import aspose.groupdocsviewer as gv
import aspose.groupdocsviewer.options as gvo
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = os.path.join(output_directory, "result_page.html")

    # TO HTML
    with gv.Viewer(test_files.sample_visio) as viewer:
        html_options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        html_options.visio_rendering_options.render_figures_only = True
        html_options.visio_rendering_options.figure_width = 250

        viewer.view(html_options)

    page_file_path_format = os.path.join(output_directory, "visio_result.jpg")

    # TO JPG
    with gv.Viewer(test_files.sample_visio) as viewer:
        jpg_options = gvo.JpgViewOptions(page_file_path_format)
        jpg_options.visio_rendering_options.render_figures_only = True
        jpg_options.visio_rendering_options.figure_width = 250

        viewer.view(jpg_options)

    page_file_path_format = os.path.join(output_directory, "visio_result.png")

    # TO PNG
    with gv.Viewer(test_files.sample_visio) as viewer:
        png_options = gvo.PngViewOptions(page_file_path_format)
        png_options.visio_rendering_options.render_figures_only = True
        png_options.visio_rendering_options.figure_width = 250

        viewer.view(png_options)

    page_file_path_format = os.path.join(output_directory, "visio_result.pdf")

    # TO PDF
    with gv.Viewer(test_files.sample_visio) as viewer:
        pdf_options = gvo.PdfViewOptions(page_file_path_format)
        pdf_options.visio_rendering_options.render_figures_only = True
        pdf_options.visio_rendering_options.figure_width = 250

        viewer.view(pdf_options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
