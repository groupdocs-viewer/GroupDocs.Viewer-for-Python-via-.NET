# get_view_info_for_cad_drawing.py
# Get a list of all layouts and layers of a CAD drawing

import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import groupdocs.viewer.results as gvr
from groupdocs.pycore import *
import os
from os.path import join
import test_files
import utils

def run():
    with gv.Viewer(test_files.sample_dwg_with_layouts_and_layers) as viewer:
        view_info_options = gvo.ViewInfoOptions.for_html_view()
        # Default value is False, so only Model is rendered by default
        # Set RenderLayouts to True to include all layouts
        # See https://docs.groupdocs.com/viewer/net/render-all-layouts/
        view_info_options.cad_options.render_layouts = True

        view_info = viewer.get_view_info(view_info_options)
        cad_info = cast(gvr.CadViewInfo, view_info)

        print("Document type is: " + str(cad_info.file_type))
        print("Pages count: " + str(len(cad_info.pages)))

        print("\nLayouts:")
        for layout in cad_info.layouts:
            print(layout)

        print("\nLayers:")
        for layer in cad_info.layers:
            print(layer)

    print("\nCAD info obtained successfully.")

if __name__ == "__main__":
    run()
