# rendering_pc3_files.py
# This example demonstrates how to render CAD drawings with PC3 configuration to JPG.

import aspose.groupdocsviewer as gv
import aspose.groupdocsviewer.options as gvo
import os
from os.path import join
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = join(output_directory, "pc3_result.jpg")

    with gv.Viewer(test_files.sample_dwg_with_layouts_and_layers) as viewer:
        jpg_options = gvo.JpgViewOptions(page_file_path_format)        
        jpg_options.cad_options.pc_3_file = test_files.sample_pc3_config

        viewer.view(jpg_options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}")

if __name__ == "__main__":
    run()
