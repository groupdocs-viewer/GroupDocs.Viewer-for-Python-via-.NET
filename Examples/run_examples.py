from quick_start import *
from basic_usage import *
from advanced_usage import *


if __name__ == '__main__':
    ## Quick Start
    set_license_from_file.run()  
    # set_license_from_stream.run()
    # set_metered_license.run()
    hello_world.run()

    ## Basic Usage    
    check_file_is_encrypted.run() 
    get_supported_file_formats.run()
    get_view_info.run()
    
    # Processing attachments
    render_document_attachments.run()
    retrieve_and_print_document_attachments.run()
    retrieve_and_save_document_attachments.run()
            
    # Render document to HTML
    excluding_fonts_from_output_html.run()
    minify_html_document.run()
    render_to_html_with_embedded_resources.run()
    render_to_html_with_external_resources.run()
    render_to_responsive_html.run()
    
    # Render document to Image
    adjust_image_size.run()    
    adjust_quality_when_rendering_to_jpg.run()
    get_text_coordinates.run()
    render_for_display_with_text.run()
    render_to_jpg.run()
    render_to_png.run()
    
    # Render document to PDF
    adjust_quality_of_jpg_images.run()
    protect_pdf_document.run() 
    render_to_pdf.run()

    ## Advanced Usage
    # Common rendering options
    add_watermark.run()
    flip_rotate_pages.run()
    render_document_with_comments.run()
    render_document_with_notes.run()
    render_hidden_pages.run()
    render_n_consecutive_pages.run()
    render_selected_pages.run()
    # render_with_custom_fonts.run() # TODO
    reorder_pages.run()
    replace_missing_font.run()
    set_image_size_limits.run()

    # Rendering Archive files
    get_view_info_for_archive_file.run()
    render_archive_folder.run()
    rendering_archives_to_multiple_and_single_pages_html.run()
    rendering_rar.run()
    specify_filename_when_rendering_archive_files.run()
    
    # Rendering CAD drawings
    adjust_output_image_size.run()
    get_view_info_for_cad_drawing.run()
    render_all_layouts.run()
    render_layers.run() 
    render_single_layout.run()
    rendering_cf2.run()
    rendering_hpg.run()
    rendering_igs.run()
    rendering_obj.run()
    rendering_pc3_files.run()
    rendering_plt.run()
    set_image_background_color.run()
    split_drawing_into_tiles.run()

    # Rendering Email messages
    adjust_page_size.run()
    datetime_format_and_time_zone_offset.run()
    # rename_email_fields.run() # TODO - NOT SUPPORTED
    
    # Rendering Image files
    # rendering_ai.run() # TODO
    rendering_apng.run()
    rendering_cdr.run()    
    rendering_cmx.run()
    rendering_emz_and_emf.run()    
    rendering_fodg_and_odg.run() 
    rendering_svgz.run()    
    rendering_tga.run()
    rendering_wmz_wmf.run()
    
    # Rendering Lotus Notes data files
    filter_lotus_notes_messages.run()
    rendering_nsf.run()              
   
    # Rendering MS Project documents
    adjust_time_unit.run()
    get_view_info_for_project_document.run() 
    render_project_time_interval.run()
    rendering_notes.run()

    # Rendering Outlook data files
    filter_messages.run()
    get_view_info_for_outlook_data_file.run()
    limit_count_of_items_to_render.run()
    render_outlook_data_file_folder.run()
    rendering_pst_and_ost.run()

    # Rendering PDF documents
    adjust_image_quality.run()
    disable_characters_grouping.run()
    disable_text_selection.run()
    enable_font_hinting.run()
    enable_layered_rendering.run()
    get_view_info_for_pdf_document.run()
    render_original_page_size.run()

    # Rendering Presentation documents
    rendering_fodp.run()

    # Rendering Spreadsheets
    adjust_text_overflow_in_cells.run()
    get_worksheets_names.run()
    render_grid_lines.run()
    render_hidden_rows_and_columns.run()
    render_print_areas.run()
    render_row_and_column_headings.run()
    rendering_by_page_breaks.run()
    rendering_numbers.run()
    rendering_xml_spreadsheetml.run()
    skip_rendering_of_empty_columns.run()
    skip_rendering_of_empty_rows.run()
    split_worksheets_into_pages.split_by_rows()
    split_worksheets_into_pages.split_by_rows_and_columns()

    # Rendering Text files
    rendering_txt.run()

    # Rendering Visio Documents
    rendering_visio_documents_figures.run()

    # Rendering Web documents
    rendering_chm_files.run()
    rendering_html_with_user_defined_margins.run()
    
    # Rendering Word processing documents
    render_tracked_changes.run()


    ## Loading
    load_documents_with_encoding.run()
    load_password_protected_document.run()
    set_resource_loading_timeout.run()
    specify_file_type_when_loading_document.run()

    # Loading documents from different sources
    load_document_from_local_disk.run()
    load_document_from_stream.run()
    load_document_from_url.run()
    
    
    
    




          