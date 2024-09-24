# set_image_background_color.py
# This example demonstrates how to adjust output image size and set a background color when rendering CAD drawings.

import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import groupdocs.viewer.drawing as drawing
#from groupdocs.pycore import *
import os
from os.path import join
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = join(output_directory, "page_{0}.png")

    with gv.Viewer(test_files.sample_dwg_with_layouts_and_layers) as viewer:
        png_options = gvo.PngViewOptions(page_file_path_format)
        png_options.cad_options = gvo.CadOptions.for_rendering_by_width(800)      
        png_options.cad_options.background_color = drawing.Argb32Color.from_rgb(0, 128, 0)  # RGB color for green 
        viewer.view(png_options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}")

if __name__ == "__main__":
    run()
