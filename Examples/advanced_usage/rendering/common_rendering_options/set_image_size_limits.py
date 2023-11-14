# This example demonstrates how to set output image size limits when rendering documents to JPG/PNG.

import os
import aspose.groupdocsviewer as gv
import aspose.groupdocsviewer.options as gvo
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    output_file = os.path.join(output_directory, "result_image_size_limit.jpg")

    with gv.Viewer(test_files.sample_cf2) as viewer:
        jpg_options = gvo.JpgViewOptions(output_file)
        jpg_options.max_width = 400

        viewer.view(jpg_options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
