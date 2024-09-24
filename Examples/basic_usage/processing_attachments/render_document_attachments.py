# render_document_attachments.py
# This example demonstrates how to render email message attachments into HTML.

import os
import io
import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()

    with gv.Viewer(test_files.sample_msg_with_attachments) as viewer:
        attachments = viewer.get_attachments()

        for attachment in attachments:
            attachment_stream = io.BytesIO()
            viewer.save_attachment(attachment, attachment_stream)
            render_attachment(attachment, attachment_stream, output_directory)       

    print(f"\nAttachment rendered successfully.\nCheck output in {output_directory}.")

def render_attachment(attachment, attachment_stream, output_directory):
    page_file_path_format = os.path.join(output_directory, "page_{0}.html")

    extension = os.path.splitext(attachment.file_name)[1]
    file_type = gv.FileType.from_extension(extension)
    load_options = gvo.LoadOptions(file_type)

    with gv.Viewer(attachment_stream, load_options) as viewer:
        html_options = gvo.HtmlViewOptions.for_embedded_resources(page_file_path_format)

        viewer.view(html_options)

if __name__ == "__main__":
    run()
