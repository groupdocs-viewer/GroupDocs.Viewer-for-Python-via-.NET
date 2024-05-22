# rendering_xml_spreadsheetml.py
# This example demonstrates how to render an Excel 2003 SpreadSheetML XML document into HTML, JPG, PNG, PDF.

import os
from os.path import join
import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import test_files
import utils

def run():
    output_directory = utils.get_output_directory_path()
    page_file_full_path = join(output_directory, "Excel_2003_Xml_result.html")

    # Because the XML extension is associated with both an XML text document and Excel 2003 XML SpreadSheetML,
    # please specify the Excel2003XML fileType explicitly to render it as Excel 2003 XML SpreadSheetML.
    load_options = gvo.LoadOptions(gv.FileType.EXCEL_2003XML)
    
    # TO MULTI PAGES HTML
    with gv.Viewer(test_files.sample_xml_spreadsheetml, load_options) as viewer:
        options = gvo.HtmlViewOptions.for_embedded_resources(page_file_full_path)
        viewer.view(options)

    # TO JPG
    page_file_full_path = join(output_directory, "Excel_2003_Xml_result.jpg")

    with gv.Viewer(test_files.sample_xml_spreadsheetml, load_options) as viewer:
        options = gvo.JpgViewOptions(page_file_full_path)
        viewer.view(options)

    # TO PNG
    page_file_full_path = join(output_directory, "Excel_2003_Xml_result.png")

    with gv.Viewer(test_files.sample_xml_spreadsheetml, load_options) as viewer:
        options = gvo.PngViewOptions(page_file_full_path)
        viewer.view(options)

    # TO PDF
    page_file_full_path = join(output_directory, "Excel_2003_Xml_result.pdf")

    with gv.Viewer(test_files.sample_xml_spreadsheetml, load_options) as viewer:
        options = gvo.PdfViewOptions(page_file_full_path)
        viewer.view(options)

    print(f"\nSource document rendered successfully.\nCheck output in {output_directory}.")

if __name__ == "__main__":
    run()
