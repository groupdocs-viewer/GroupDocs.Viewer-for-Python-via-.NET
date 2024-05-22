# filter_lotus_notes_messages.py
# This example demonstrates how to filter messages by text/sender/recipient when rendering Lotus Notes data files.

import os
import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_path_format = os.path.join(output_directory, "page_{0}.html")

    with gv.Viewer(test_files.sample_nsf) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)

        options.mail_storage_options.text_filter = "Viewer"
        #options.mail_storage_options.address_filter = "groupdocs.com" # TODO The specified string is not in the form required for an e-mail address.
        viewer.view(options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
