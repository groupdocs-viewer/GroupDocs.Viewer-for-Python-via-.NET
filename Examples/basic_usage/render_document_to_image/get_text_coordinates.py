# get_text_coordinates.py
# This example demonstrates how to extract text from a document.

import aspose.groupdocsviewer as gv
import aspose.groupdocsviewer.options as gvo
import os
from os.path import join
import test_files

def run():
    with gv.Viewer(test_files.sample_docx) as viewer:
        view_info_options = gvo.ViewInfoOptions.for_png_view(True)
        view_info = viewer.get_view_info(view_info_options)

        for page in view_info.pages:
            print(f"Page: {page.number}")
            print("Text lines/words/characters:")

            for line in page.lines:
                print(line)
                for word in line.words:
                    print("\t" + word.value)
                    for character in word.characters:
                        print("\t\t" + character.value)

    print("\nDocument text extracted successfully.\n")

if __name__ == "__main__":
    run()
