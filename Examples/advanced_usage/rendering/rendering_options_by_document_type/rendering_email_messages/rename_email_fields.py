# rename_email_fields.py
# This example demonstrates how to rename fields when rendering email messages.

import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import os
from os.path import join
import test_files
import utils

def run():
    # Update with the path to your output directory
    output_directory = utils.get_output_directory_path()

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    page_file_path_format = join(output_directory, "page_{0}.html")

    with gv.Viewer(test_files.sample_msg) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)
        # TODO - NOT SUPPORTED CURRENTLY - The member data type 'System.Collections.Generic.Dictionary<GroupDocs.Viewer.Options.Field,System.String>' is not sutable for exchanging between Python and .Net contexts
        options.email_options.field_text_map[gvo.Field.FROM] = "Sender"
        options.email_options.field_text_map[gvo.Field.TO] = "Receiver"
        options.email_options.field_text_map[gvo.Field.SENT] = "Date"
        options.email_options.field_text_map[gvo.Field.SUBJECT] = "Topic"

        viewer.view(options)

    # Indicate the successful rendering of the source document and specify where to find the output in the specified directory
    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
