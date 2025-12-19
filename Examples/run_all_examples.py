import os
import subprocess
import sys

# Set license path (update this path to your license file location)
# os.environ["GROUPDOCS_LIC_PATH"] = "./GroupDocs.Viewer.lic"

# Console output colors
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def print_intro():
    intro_text = """
=================================================================
Welcome to the GroupDocs.Viewer for Python via .NET Examples!
=================================================================

This script will run a series of examples showcasing the features of GroupDocs.Viewer for Python via .NET.
Each example demonstrates different use cases and functionalities such as:

- Rendering documents to HTML, PDF, PNG, JPEG.
- Retrieving document information.
- Handling password-protected files.
- Working with file containers and archives.
- Setting and managing licenses.

Enjoy exploring the GroupDocs API! 

=======================================================
"""
    print(intro_text)

def set_license():
    """Set the GroupDocs license from environment variable or license file."""
    from groupdocs.viewer import License
    
    # First, check for license path in environment variable
    license_path = os.environ.get("GROUPDOCS_LIC_PATH")
    
    # Set license if found
    if license_path and os.path.exists(license_path):
        license = License()
        license.set_license(license_path)
        print(f"{GREEN}License set from: {license_path}{RESET}\n")
    else:
        print(f"{YELLOW}No license file found. Running in evaluation mode.{RESET}\n")

examples = [
    "getting-started/hello-world/render_docx_to_html.py",
    "getting-started/hello-world/render_docx_to_pdf.py",
    "getting-started/hello-world/render_docx_to_png.py",
    "licensing/set_license_from_file.py",
    "licensing/set_license_from_stream.py",
    "licensing/set_metered_license.py",
    "rendering-basics/render-spreadsheets/render-excel-and-apple-numbers-spreadsheets/render_excel_to_html.py",
    "rendering-basics/render-spreadsheets/render-excel-and-apple-numbers-spreadsheets/render_numbers_to_html.py",
    "rendering-basics/render-spreadsheets/render-excel-and-apple-numbers-spreadsheets/render_excel_to_html_external.py",
    "rendering-basics/render-spreadsheets/render-excel-and-apple-numbers-spreadsheets/render_numbers_to_html_external.py",
    "rendering-basics/render-spreadsheets/render-excel-and-apple-numbers-spreadsheets/render_excel_to_single_html.py",
    "rendering-basics/render-spreadsheets/render-excel-and-apple-numbers-spreadsheets/render_excel_to_pdf.py",
    "rendering-basics/render-spreadsheets/render-excel-and-apple-numbers-spreadsheets/render_numbers_to_pdf.py",
    "rendering-basics/render-spreadsheets/render-excel-and-apple-numbers-spreadsheets/render_excel_to_png.py",
    "rendering-basics/render-spreadsheets/render-excel-and-apple-numbers-spreadsheets/render_numbers_to_png.py",
    "rendering-basics/render-spreadsheets/render-excel-and-apple-numbers-spreadsheets/render_excel_to_jpg.py",
    "rendering-basics/render-spreadsheets/render-excel-and-apple-numbers-spreadsheets/render_numbers_to_jpg.py",
    "rendering-basics/render-spreadsheets/render-excel-and-apple-numbers-spreadsheets/render_csv_with_separator_detection.py",
    "rendering-basics/render-spreadsheets/render-excel-and-apple-numbers-spreadsheets/get_worksheet_names.py",
    "rendering-basics/render-word-documents/render_word_to_html.py",
    "rendering-basics/render-word-documents/render_word_to_html_external.py",
    "rendering-basics/render-word-documents/render_word_to_pdf.py",
    "rendering-basics/render-word-documents/render_word_to_png.py",
    "rendering-basics/render-word-documents/render_word_to_jpg.py",
    "rendering-basics/render-word-documents/render_word_with_margins.py",
    "rendering-basics/render-word-documents/render_word_with_tracked_changes.py",
    "rendering-basics/render-word-documents/render_word_with_comments.py",
    "rendering-basics/render-pdf-documents/render_pdf_to_html.py",
    "rendering-basics/render-pdf-documents/render_pdf_to_html_external.py",
    "rendering-basics/render-pdf-documents/render_pdf_with_image_quality.py",
    "rendering-basics/render-pdf-documents/render_pdf_text_as_image.py",
    "rendering-basics/render-pdf-documents/render_pdf_with_layered_rendering.py",
    "rendering-basics/render-pdf-documents/render_pdf_to_png.py",
    "rendering-basics/render-pdf-documents/render_pdf_to_jpg.py",
    "rendering-basics/render-pdf-documents/render_pdf_preserve_page_size.py",
    "rendering-basics/render-pdf-documents/render_pdf_with_font_hinting.py",
    "rendering-basics/render-pdf-documents/render_pdf_disable_char_grouping.py",
    "rendering-basics/render-pdf-documents/render_pdf_with_comments.py",
    "rendering-basics/render-pdf-documents/get_pdf_information.py",
    "rendering-basics/render-pdf-documents/extract_pdf_text.py",
    "rendering-basics/render-spreadsheets/split-worksheet-into-pages/split_by_page_breaks.py",
    "rendering-basics/render-spreadsheets/split-worksheet-into-pages/split_by_rows.py",
    "rendering-basics/render-spreadsheets/split-worksheet-into-pages/split_by_rows_and_columns.py",
    "rendering-basics/render-spreadsheets/split-worksheet-into-pages/render_print_area.py",
    "rendering-basics/render-spreadsheets/split-worksheet-into-pages/render_one_page_per_sheet.py",
    "rendering-basics/render-spreadsheets/split-worksheet-into-pages/render_print_area_and_page_breaks.py",
    "rendering-basics/render-spreadsheets/specify-rendering-options/render_headings.py",
    "rendering-basics/render-spreadsheets/specify-rendering-options/render_grid_lines.py",
    "rendering-basics/render-spreadsheets/specify-rendering-options/set_text_overflow_mode.py",
    "rendering-basics/render-spreadsheets/specify-rendering-options/render_hidden_rows_and_columns.py",
    "rendering-basics/render-spreadsheets/specify-rendering-options/render_hidden_pages.py",
    "rendering-basics/render-spreadsheets/specify-rendering-options/skip_empty_rows_and_columns.py",
    "rendering-basics/render-spreadsheets/specify-rendering-options/render_comments.py",
    "rendering-basics/render-spreadsheets/specify-rendering-options/set_worksheet_margins.py",
    "rendering-basics/render-presentations/render_presentation_to_html.py",
    "rendering-basics/render-presentations/render_presentation_to_html_external.py",
    "rendering-basics/render-presentations/render_presentation_to_pdf.py",
    "rendering-basics/render-presentations/render_presentation_to_png.py",
    "rendering-basics/render-presentations/render_presentation_to_jpg.py",
    "rendering-basics/render-presentations/render_presentation_with_hidden_slides.py",
    "rendering-basics/render-presentations/render_presentation_with_comments.py",
    "rendering-basics/render-presentations/render_presentation_with_notes.py",
    "rendering-basics/render-visio-documents/render_visio_to_html.py",
    "rendering-basics/render-visio-documents/render_visio_to_html_external.py",
    "rendering-basics/render-visio-documents/render_visio_to_pdf.py",
    "rendering-basics/render-visio-documents/render_visio_to_png.py",
    "rendering-basics/render-visio-documents/render_visio_to_jpg.py",
    "rendering-basics/render-visio-documents/render_visio_shapes_only.py",
    "rendering-basics/render-ms-project-files/render_project_to_html.py",
    "rendering-basics/render-ms-project-files/render_project_to_html_external.py",
    "rendering-basics/render-ms-project-files/render_project_to_pdf.py",
    "rendering-basics/render-ms-project-files/render_project_to_png.py",
    "rendering-basics/render-ms-project-files/render_project_to_jpg.py",
    "rendering-basics/render-ms-project-files/get_project_info.py",
    "rendering-basics/render-ms-project-files/render_project_with_page_size.py",
    "rendering-basics/render-ms-project-files/render_project_with_time_unit.py",
    "rendering-basics/render-ms-project-files/render_project_with_notes.py",
    "rendering-basics/render-ebooks/render_ebook_to_html.py",
    "rendering-basics/render-ebooks/render_ebook_to_html_external.py",
    "rendering-basics/render-ebooks/render_ebook_to_pdf.py",
    "rendering-basics/render-ebooks/render_ebook_to_png.py",
    "rendering-basics/render-ebooks/render_ebook_to_jpg.py",
    "rendering-basics/render-web-documents/render_web_to_pdf.py",
    "rendering-basics/render-web-documents/render_web_to_png.py",
    "rendering-basics/render-web-documents/render_web_to_jpg.py",
    "rendering-basics/render-web-documents/render_chm_to_html.py",
    "rendering-basics/render-web-documents/render_chm_to_html_external.py",
    "rendering-basics/render-text-files/render_text_with_load_options.py",
    "rendering-basics/render-text-files/render_text_to_html.py",
    "rendering-basics/render-text-files/render_text_to_html_external.py",
    "rendering-basics/render-text-files/render_text_to_single_html.py",
    "rendering-basics/render-text-files/render_text_to_pdf.py",
    "rendering-basics/render-text-files/render_text_to_png.py",
    "rendering-basics/render-text-files/render_text_to_jpg.py",
    "rendering-basics/render-xml-documents/load_xml_document.py",
    "rendering-basics/render-xml-documents/load_xml_with_encoding.py",
    "rendering-basics/render-xml-documents/render_xml_to_html.py",
    "rendering-basics/render-xml-documents/render_xml_to_pdf.py",
    "rendering-basics/render-xml-documents/render_xml_to_images.py",
    "rendering-basics/render-xml-documents/get_xml_view_info.py",
    "rendering-basics/render-images/render_image_to_html.py",
    "rendering-basics/render-images/render_image_to_html_external.py",
    "rendering-basics/render-images/render_image_to_pdf.py",
    "rendering-basics/render-images/render_image_to_png.py",
    "rendering-basics/render-images/render_image_to_jpg.py",
    "rendering-basics/render-images/render_psd_with_custom_fonts.py",
    "rendering-basics/render-email-messages/render_email_to_html.py",
    "rendering-basics/render-email-messages/render_email_to_html_external.py",
    "rendering-basics/render-email-messages/render_email_to_pdf.py",
    "rendering-basics/render-email-messages/render_email_to_png.py",
    "rendering-basics/render-email-messages/render_email_to_jpg.py",
    "rendering-basics/render-email-messages/render_email_with_page_size.py",
    "rendering-basics/render-email-messages/render_email_with_datetime_format.py",
    "rendering-basics/render-outlook-data-files/render_outlook_to_html.py",
    "rendering-basics/render-outlook-data-files/render_outlook_to_pdf.py",
    "rendering-basics/render-outlook-data-files/render_outlook_to_png.py",
    "rendering-basics/render-outlook-data-files/render_outlook_to_jpg.py",
    "rendering-basics/render-outlook-data-files/render_outlook_specific_folder.py",
    "rendering-basics/render-outlook-data-files/render_outlook_with_max_items.py",
    "rendering-basics/render-outlook-data-files/render_outlook_with_filters.py",
    "rendering-basics/render-lotus-notes-files/render_nsf_to_html.py",
    "rendering-basics/render-lotus-notes-files/render_nsf_to_pdf.py",
    "rendering-basics/render-lotus-notes-files/render_nsf_to_png.py",
    "rendering-basics/render-lotus-notes-files/render_nsf_to_jpg.py",
    "rendering-basics/render-lotus-notes-files/render_nsf_with_max_items.py",
    "rendering-basics/render-lotus-notes-files/render_nsf_with_filters.py",
    "rendering-basics/render-archive-files/render_archive_to_html.py",
    "rendering-basics/render-archive-files/render_archive_with_items_per_page.py",
    "rendering-basics/render-archive-files/render_archive_to_single_html.py",
    "rendering-basics/render-archive-files/render_archive_to_pdf.py",
    "rendering-basics/render-archive-files/render_archive_to_png.py",
    "rendering-basics/render-archive-files/render_archive_to_jpg.py",
    "rendering-basics/render-archive-files/render_specific_archive_folder.py",
    "rendering-basics/render-archive-files/render_archive_with_custom_filename.py",
    "rendering-basics/render-cad-documents/render-cad-documents/render_cad_to_html.py",
    "rendering-basics/render-cad-documents/render-cad-documents/render_cad_to_html_external.py",
    "rendering-basics/render-cad-documents/render-cad-documents/render_cad_to_pdf.py",
    "rendering-basics/render-cad-documents/render-cad-documents/render_cad_to_png.py",
    "rendering-basics/render-cad-documents/render-cad-documents/render_cad_to_jpg.py",
    "rendering-basics/render-cad-documents/render-cad-documents/get_cad_info.py",
    "rendering-basics/render-cad-documents/render-cad-documents/render_all_layouts.py",
    "rendering-basics/render-cad-documents/render-cad-documents/render_specific_layout.py",
    "rendering-basics/render-cad-documents/render-cad-documents/render_specific_layers.py",
    "rendering-basics/render-cad-documents/specify-rendering-options/set_background_color.py",
    "rendering-basics/render-cad-documents/specify-rendering-options/set_image_size.py",
    "rendering-basics/render-cad-documents/specify-rendering-options/apply_pc3_file.py",
    "rendering-basics/render-cad-documents/specify-rendering-options/split_drawing_into_tiles.py",
    "rendering-basics/render-cad-documents/specify-rendering-options/enable_performance_mode.py",
    "developer-guide/loading-documents/loading-documents-from-different-sources/load-document-from-local-disk/load_document_from_local_disk.py",
    "developer-guide/loading-documents/loading-documents-from-different-sources/loading-documents-from-stream/load-document-from-url/download_file.py",
    "developer-guide/retrieving-document-information/how-to-get-file-type-and-pages-count/get_file_type_and_pages_count.py",
    "developer-guide/rendering-documents/rendering-to-pdf/optimization-pdf-options/optimization-pdf-for-web/optimize_pdf_for_web.py",
    "developer-guide/rendering-documents/rendering-to-pdf/optimization-pdf-options/optimize-content/optimization-pdf-remove-annotations/remove_annotations.py",
    "developer-guide/rendering-documents/rendering-to-pdf/optimization-pdf-options/optimize-images/optimization-pdf-reduce-image-quality/reduce_image_quality.py",
    "developer-guide/rendering-documents/rendering-to-pdf/reorder-pages/reorder_pages.py",
    "developer-guide/rendering-documents/rendering-to-pdf/optimization-pdf-options/optimization-pdf-resources/optimize_pdf_resources.py",
    "developer-guide/rendering-documents/rendering-to-pdf/optimization-pdf-options/optimize-content/optimization-pdf-remove-fields/remove_form_fields.py",
    "developer-guide/rendering-documents/rendering-to-pdf/optimization-pdf-options/optimize-fonts/optimization-pdf-subset-fonts/subset_fonts.py",
    "developer-guide/rendering-documents/rendering-to-pdf/optimization-pdf-options/optimize-images/optimization-pdf-set-max-resolution/set_max_resolution.py",
    "developer-guide/rendering-documents/rendering-to-pdf/protect-pdf-document/protect_pdf_document.py",
    "developer-guide/rendering-documents/rendering-to-pdf/adjust-jpeg-images-quality/adjust_jpeg_quality.py",
    "developer-guide/rendering-documents/rendering-to-pdf/optimization-pdf-options/optimization-pdf-spreadsheets/optimize_spreadsheets.py",
    "developer-guide/rendering-documents/rendering-to-pdf/optimization-pdf-options/optimize-images/optimization-pdf-convert-grayscale/convert_to_grayscale.py",
    "developer-guide/rendering-documents/rendering-to-pdf/set-image-size-limits-when-rendering-to-pdf/set_image_size_limits.py",
    "developer-guide/rendering-documents/add-text-watermark/add_text_watermark.py",
    "developer-guide/rendering-documents/rendering-to-pdf/optimization-pdf-options/pdf-remove-unused-resources/remove_unused_resources.py",
    "developer-guide/processing-attachments/how-to-extract-and-save-attachments/extract_and_save_attachments.py",
]

print_intro()
set_license()

# Get current environment variables from the parent process
env = os.environ.copy()

# Run each example script
for example in examples:
    current_dir = os.path.dirname(__file__)
    example_path = os.path.join(current_dir, example)
    example_dir = os.path.dirname(example_path)

    print(f"{YELLOW}Running {example}...{RESET}")
    try:
        # Execute the example script in the current environment
        subprocess.run(
            [sys.executable, example_path], 
            cwd=example_dir, 
            check=True, 
            env=env
        )
        print(f"{GREEN}Completed {example}{RESET}\n")
    except subprocess.CalledProcessError as e:
        print(f"{RED}Error running {example}: {e}{RESET}\n")
