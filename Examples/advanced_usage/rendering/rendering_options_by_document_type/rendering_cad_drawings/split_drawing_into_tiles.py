# split_drawing_into_tiles.py
# This example demonstrates how to split drawing into tiles.

import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import os
from os.path import join
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = join(output_directory, "page_{0}.png")

    with gv.Viewer(test_files.sample_dwg_with_layouts_and_layers) as viewer:
        info_options = gvo.ViewInfoOptions.for_png_view(False)
        view_info = viewer.get_view_info(info_options)

        # Get width and height
        width = view_info.pages[0].width
        height = view_info.pages[0].height

        # Set tile width and height as a half of image total width
        tile_width = width // 2
        tile_height = height // 2

        point_x = 0
        point_y = 0

        # Create image options and add four tiles, one for each quarter
        png_options = gvo.PngViewOptions(page_file_path_format)

        tile = gvo.Tile(point_x, point_y, tile_width, tile_height)
        png_options.cad_options.tiles.append(tile)

        point_x += tile_width
        tile = gvo.Tile(point_x, point_y, tile_width, tile_height)
        png_options.cad_options.tiles.append(tile)

        point_x = 0
        point_y += tile_height
        tile = gvo.Tile(point_x, point_y, tile_width, tile_height)
        png_options.cad_options.tiles.append(tile)

        point_x += tile_width
        tile = gvo.Tile(point_x, point_y, tile_width, tile_height)
        png_options.cad_options.tiles.append(tile)

        viewer.view(png_options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}")

if __name__ == "__main__":
    run()
