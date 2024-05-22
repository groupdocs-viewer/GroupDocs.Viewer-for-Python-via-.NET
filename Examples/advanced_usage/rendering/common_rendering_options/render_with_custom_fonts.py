# render_with_custom_fonts.py
# This example demonstrates how to add custom fonts to use when rendering documents.

import os
import groupdocs.viewer as gv
import groupdocs.viewer.fonts as gvf
import groupdocs.viewer.options as gvo
import test_files
import utils

def run():
    fonts_path = utils.fonts_path   
    gvf.FontSettings.set_font_sources([gvf.FolderFontSource(fonts_path, gvf.SearchOption.TOP_FOLDER_ONLY)]) 

    output_directory = utils.get_output_directory_path()
    page_file_path_format = os.path.join(output_directory, "page_{0}.html")

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with gv.Viewer(test_files.missing_font_odg) as viewer:
        html_options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        viewer.view(html_options)

    # TODO:  RuntimeError: Proxy error(FileNotFoundException): Could not load file or assembly 'System.Drawing.Common, Version=6.0.0.0, Culture=neutral, PublicKeyToken=cc7b13ffcd2ddd51'. �� ������� ����� ��������� ����.
    
    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
