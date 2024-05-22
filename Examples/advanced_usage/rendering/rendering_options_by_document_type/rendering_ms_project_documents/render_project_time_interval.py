# render_project_time_interval.py
# This example demonstrates how to render project document within the specified time interval.

import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import groupdocs.viewer.results as gvr
from datetime import timedelta
from groupdocs.pycore import *
import os
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = os.path.join(output_directory, "page_{0}.html")

    with gv.Viewer(test_files.sample_mpp) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)

        view_info_options = gvo.ViewInfoOptions.from_html_view_options(options)
        view_info = viewer.get_view_info(view_info_options)  # Получите информацию о документе

        info = cast(gvr.ProjectManagementViewInfo, view_info)   
        options.project_management_options.start_date = info.start_date
        options.project_management_options.end_date = info.start_date + timedelta(days=7)  # Настройте временной интервал

        viewer.view(options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
