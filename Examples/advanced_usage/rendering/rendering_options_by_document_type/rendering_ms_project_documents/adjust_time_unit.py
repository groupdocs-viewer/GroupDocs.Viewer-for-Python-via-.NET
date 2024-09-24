# adjust_time_unit.py
# This example demonstrates how to adjust the time unit of the project.

import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import os
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = os.path.join(output_directory, "page_{0}.html")

    with gv.Viewer(test_files.sample_mpp) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        options.project_management_options.time_unit = gvo.TimeUnit.DAYS

        viewer.view(options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
