# adjust_image_quality.py
# This example demonstrates how to adjust the quality of images contained in the source PDF document.

import os
from os.path import join
import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = join(output_directory, "page_{0}.html")

    with gv.Viewer(test_files.sample_pdf) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        options.pdf_options.image_quality = gvo.ImageQuality.MEDIUM 

        viewer.view(options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()

# /*
# [enum]: ImageQuality

#             <fullname>: groupdocs.viewer.options.ImageQuality

#             <original>: GroupDocs.Viewer.Options.ImageQuality

#             [values]:

#                 LOW -> Low

#                 MEDIUM -> Medium

#                 HIGH -> High
# */