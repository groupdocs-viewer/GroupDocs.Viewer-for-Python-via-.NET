from groupdocs.viewer import Viewer
from groupdocs.viewer.options import ViewInfoOptions

def get_xml_view_info():
    # Create view info options for HTML format (single page)
    view_info_options_html_single = ViewInfoOptions.for_html_view(True)
    # Create view info options for PDF format
    view_info_options_pdf = ViewInfoOptions.for_pdf_view()
    # Create view info options for PNG format
    view_info_options_png = ViewInfoOptions.for_png_view()

    # Load XML document
    with Viewer("sample.xml") as viewer:
        # Get view information for HTML format (single page)
        result_html_single = viewer.get_view_info(view_info_options_html_single)  
        # Get view information for PDF format
        result_pdf = viewer.get_view_info(view_info_options_pdf) 
        # Get view information for PNG format
        result_png = viewer.get_view_info(view_info_options_png)

if __name__ == "__main__":
    get_xml_view_info()