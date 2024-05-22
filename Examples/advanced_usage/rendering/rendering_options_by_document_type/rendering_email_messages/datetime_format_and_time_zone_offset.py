# datetime_format_and_time_zone_offset.py
# This example demonstrates how to set custom date-time format and time zone offset

import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import os
from os.path import join
import test_files
import utils
from datetime import timedelta

def run():
    output_directory = utils.get_output_directory_path()
    file_path = join(output_directory, "output.html")

    with gv.Viewer(test_files.sample_eml) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(file_path)
        options.email_options.date_time_format = "MM d yyyy HH:mm tt zzz"
        options.email_options.time_zone_offset = timedelta(hours=1)

        viewer.view(options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}")

if __name__ == "__main__":
    run()
