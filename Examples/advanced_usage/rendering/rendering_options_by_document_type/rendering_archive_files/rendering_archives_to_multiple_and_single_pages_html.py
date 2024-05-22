# rendering_archives_to_multiple_and_single_pages_html.py
# This example demonstrates how to render archive files into multiple/single pages HTML.

import os
import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = os.path.join(output_directory, "RAR_result.html")

    # TO single page HTML
    with gv.Viewer(test_files.sample_rar_with_folders) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        options.render_to_single_page = True

        viewer.view(options)

    # RAR_result_page_{0}.html - {0} is the page number mask
    page_file_path_format = os.path.join(output_directory, "RAR_result_page_{0}.html")

    # TO multi pages HTML
    with gv.Viewer(test_files.sample_rar_with_folders) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)

        """
        If options.render_to_single_page is set to False (by default),
        you can set the number of items per page (default is 16), this property is for rendering to HTML only
        """
        options.archive_options.items_per_page = 10

        viewer.view(options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
