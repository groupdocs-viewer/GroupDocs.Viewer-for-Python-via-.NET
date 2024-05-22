# This example demonstrates how to retrieve and print all attachments.

import groupdocs.viewer as gv
import test_files

def run():
    with gv.Viewer(test_files.sample_msg_with_attachments) as viewer:
        attachments = viewer.get_attachments()

        print("\nAttachments:")
        for attachment in attachments:
            print(attachment)

    print(f"\nAttachments retrieved successfully.")

if __name__ == "__main__":
    run()
