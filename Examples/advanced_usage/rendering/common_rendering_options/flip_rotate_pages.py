# flip_rotate_pages.py
# This example demonstrates how to rotate the first page 90 degrees clockwise.

import os
import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
#import groupdocs.viewer.rotation as rotation
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    output_file_path = os.path.join(output_directory, "output.pdf")

    with gv.Viewer(test_files.sample_docx) as viewer:
        pdf_options = gvo.PdfViewOptions(output_file_path)
# mod = getattr(parent_mod, parts[-1])
# AttributeError: cannot access submodule 'rotation' of module 'groupdocs.viewer' (most likely due to a circular import)
        #pdf_options.rotate_page(1, rotation.Rotation.on_90_degree)

        viewer.view(pdf_options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
