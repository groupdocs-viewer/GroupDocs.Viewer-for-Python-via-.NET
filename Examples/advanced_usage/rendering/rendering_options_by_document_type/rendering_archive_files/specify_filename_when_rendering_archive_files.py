# specify_filename_when_rendering_archive_files.py
# This example demonstrates how to specify filename when rendering archive files.

import os
import aspose.groupdocsviewer as gv
import aspose.groupdocsviewer.options as gvo
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    output_file_path = os.path.join(output_directory, "output.pdf")

    with gv.Viewer(test_files.sample_zip) as viewer:
        view_options = gvo.PdfViewOptions(output_file_path)
        view_options.archive_options.file_name = gvo.FileName("my filename")

        viewer.view(view_options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
