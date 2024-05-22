# render_single_layout.py
# This example demonstrates how to render a specific layout.

import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import os
from os.path import join
import test_files
import utils

def render_layout(output_directory, input_file, layout_name):
    page_file_path_format = join(output_directory, f"page_{layout_name}.html")

    with gv.Viewer(input_file) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        options.cad_options.layout_name = layout_name

        viewer.view(options)

def run():
    output_directory = utils.get_output_directory_path()
    layout_name = "Model"  # Replace with the name of the layout you want to render

    render_layout(output_directory, test_files.sample_dwg_with_layouts_and_layers, layout_name)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
