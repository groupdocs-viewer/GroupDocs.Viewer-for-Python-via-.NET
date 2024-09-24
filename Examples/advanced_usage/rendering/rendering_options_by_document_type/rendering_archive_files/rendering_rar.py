# rendering_rar.py
# This example demonstrates how to render RAR document into HTML, JPG, PNG, PDF.

import os
import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import groupdocs.viewer.results as gvr
from groupdocs.pycore import *
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = os.path.join(output_directory, "RAR_result_{0}.html")

    # TO HTML
    with gv.Viewer(test_files.sample_rar_with_folders) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)

        viewer.view(options)

    # TO JPG
    page_file_path_format = os.path.join(output_directory, "RAR_result_{0}.jpg")

    with gv.Viewer(test_files.sample_rar_with_folders) as viewer:
        options = gvo.JpgViewOptions(page_file_path_format)

        viewer.view(options)

    # TO PNG
    page_file_path_format = os.path.join(output_directory, "RAR_result_{0}.png")

    with gv.Viewer(test_files.sample_rar_with_folders) as viewer:
        options = gvo.PngViewOptions(page_file_path_format)

        viewer.view(options)

    # TO PDF
    page_file_path_format = os.path.join(output_directory, "RAR_result.pdf")

    with gv.Viewer(test_files.sample_rar_with_folders) as viewer:
        options = gvo.PdfViewOptions(page_file_path_format)

        viewer.view(options)

    get_view_info_for_rar()
    render_specific_archive_folder()

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

def get_view_info_for_rar():
    with gv.Viewer(test_files.sample_rar_with_folders) as viewer:
        info = viewer.get_view_info(gvo.ViewInfoOptions.for_html_view())

        print("File type: " + str(info.file_type))
        print("Pages count: " + str(len(info.pages)))

        print("Folders: ")
        print(" - /")

        root_folder = ""
        read_folders(viewer, root_folder)

    print("\nView info retrieved successfully.")

def render_specific_archive_folder():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = os.path.join(output_directory, "archive_folder_page_{0}.html")

    with gv.Viewer(test_files.sample_rar_with_folders) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        options.archive_options.folder = os.path.join("with_folders", "ThirdFolderWithItems")
        viewer.view(options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

def read_folders(viewer, folder):
    options = gvo.ViewInfoOptions.for_html_view()
    options.archive_options.folder = folder

    info = viewer.get_view_info(options)
    view_info = cast(gvr.ArchiveViewInfo, info)    

    for sub_folder in view_info.folders:
        print(f" - {sub_folder}")

if __name__ == "__main__":
    run()
