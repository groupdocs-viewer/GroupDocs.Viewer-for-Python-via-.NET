# retrieve_and_save_document_attachments.py
# This example demonstrates how to retrieve and save attachments.

import os
import aspose.groupdocsviewer as gv
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()

    with gv.Viewer(test_files.sample_msg_with_attachments) as viewer:
        attachments = viewer.get_attachments()
        
        for attachment in attachments:
            file_path = os.path.join(output_directory, attachment.file_name)

            with open(file_path, 'wb') as attachment_file:
                viewer.save_attachment(attachment, attachment_file)

    print(f"\nAttachments saved successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()