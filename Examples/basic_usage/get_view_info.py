import groupdocs.viewer as gv
import groupdocs.viewer.options as gvo
import test_files

def run():
    with gv.Viewer(test_files.sample_pdf) as viewer:
        info = viewer.get_view_info(gvo.ViewInfoOptions.for_html_view())
        print(info)

    print("\nView info retrieved successfully.")
