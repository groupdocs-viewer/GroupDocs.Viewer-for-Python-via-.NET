# test_files.py
# This module defines paths to test files.

import os
from os.path import join
import platform
import utils

def get_sample_file_path(file_path):
    if platform.system() == 'Windows':
        return join(utils.samples_path, file_path)
    else:
        entry_dir = os.path.dirname(__file__)
        return join(entry_dir, utils.samples_path, file_path)

# Archives
sample_zip = get_sample_file_path("sample.zip")
sample_zip_with_folders = get_sample_file_path("with_folders.zip")
sample_rar_with_folders = get_sample_file_path("with_folders.rar")

# CAD drawings
sample_dwg_with_layouts_and_layers = get_sample_file_path("with_layers_and_layouts.dwg")
sample_ai = get_sample_file_path("sample.ai")
sample_plt = get_sample_file_path("sample.plt")
sample_cf2 = get_sample_file_path("sample.cf2")
sample_igs = get_sample_file_path("sample.igs")
sample_obj = get_sample_file_path("sample.obj")
sample_hpg = get_sample_file_path("sample.hpg")
sample_pc3_config = get_sample_file_path("small_page.pc3")

# Email messages
sample_msg = get_sample_file_path("sample.msg")
sample_msg_with_attachments = get_sample_file_path("with_attachments.msg")
sample_ost = get_sample_file_path("sample.ost")
sample_pst = get_sample_file_path("sample.pst")
sample_ost_subfolders = get_sample_file_path("with_subfolders.ost")
sample_nsf = get_sample_file_path("sample.nsf")
sample_eml = get_sample_file_path("sample.eml")

# PDFs
sample_pdf = get_sample_file_path("sample.pdf")
hieroglyphs_pdf = get_sample_file_path("hieroglyphs.pdf")
hieroglyphs_1_pdf = get_sample_file_path("hieroglyphs_1.pdf")
encrypted = get_sample_file_path("encrypted.pdf")
one_page_text_pdf = get_sample_file_path("one-page-text.pdf")

# Presentations
pptx_with_notes = get_sample_file_path("with_notes.pptx")
sample_pptx_hidden_page = get_sample_file_path("with_hidden_page.pptx")
missing_font_pptx = get_sample_file_path("with_missing_font.pptx")
jpg_image_pptx = get_sample_file_path("with_jpg_image.pptx")
sample_fodp = get_sample_file_path("sample.fodp")

# Project Management documents
sample_mpp = get_sample_file_path("sample.mpp")

# Visio files
sample_visio = get_sample_file_path("sample.vssx")

# Spreadsheets
sample_xlsx = get_sample_file_path("sample.xlsx")
sample_xlsx_with_print_areas = get_sample_file_path("with_four_print_areas.xlsx")
page_breaks_xlsx = get_sample_file_path("page-breaks.xlsx")
sample_xlsx_with_empty_column = get_sample_file_path("with_empty_column.xlsx")
sample_xlsx_with_empty_row = get_sample_file_path("with_empty_row.xlsx")
sample_xlsx_with_hidden_row_and_column = get_sample_file_path("with_hidden_row_and_column.xlsx")
sample_xlsx_with_text_overflow = get_sample_file_path("with_overflowing_text.xlsx")
three_sheets = get_sample_file_path("three_sheets.xlsx")
sample_numbers = get_sample_file_path("sample.numbers")
sample_xml_spreadsheetml = get_sample_file_path("excel-2003-xml.xml")
two_pages_xlsx = get_sample_file_path("two-pages.xlsx")
four_pages_xlsx = get_sample_file_path("four-pages.xlsx")

# Word Processing documents
sample_docx = get_sample_file_path("sample.docx")
sample_docx_with_comment = get_sample_file_path("with_comment.docx")
sample_docx_with_password = get_sample_file_path("password_protected.docx")
sample_docx_with_tracked_changes = get_sample_file_path("with_tracked_changes.docx")
sample_txt_shift_js_encoded = get_sample_file_path("shift_jis_encoded.txt")
with_external_image_doc = get_sample_file_path("with_external_image.doc")
sample_html = get_sample_file_path("sample.html")

# Text
sample_txt = get_sample_file_path("sample.txt")
sample_2_txt = get_sample_file_path("sample2.txt")

# Graphics
missing_font_odg = get_sample_file_path("with_missing_font.odg")
sample_fodg = get_sample_file_path("sample.fodg")
sample_svgz = get_sample_file_path("sample.svgz")
sample_wmz = get_sample_file_path("sample.wmz")
sample_emz = get_sample_file_path("sample.emz")
sample_cdr = get_sample_file_path("sample.cdr")
sample_cmx = get_sample_file_path("sample.cmx")
sample_tga = get_sample_file_path("sample.tga")
sample_apng = get_sample_file_path("sample.apng")

# Web
sample_chm = get_sample_file_path("sample.chm")


    