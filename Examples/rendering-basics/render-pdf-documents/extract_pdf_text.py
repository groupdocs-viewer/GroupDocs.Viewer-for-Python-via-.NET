import sys
from typing import cast
from groupdocs.viewer import Viewer
from groupdocs.viewer.options import ViewInfoOptions
from groupdocs.viewer.results import PdfViewInfo

def extract_pdf_text():
    # Load PDF document
    with Viewer("sample.pdf") as viewer:
        view_info_options = ViewInfoOptions.for_html_view()
        view_info_options.extract_text = True

        view_info = viewer.get_view_info(view_info_options)
        pdf_info = cast(PdfViewInfo, view_info)

        # Retrieve text from the PDF file.
        sys.stdout.reconfigure(encoding='utf-8')

        for page in pdf_info.pages:
            print(f"Page: {page.number}")
            print("Text lines/words/characters:")

            for line in page.lines:
                text = str(line)
                encoded_line = text.encode('utf-8')
                sys.stdout.buffer.write(encoded_line)

                # Collect words as array
                words = [word.value for word in line.words]
                print("\tWords:", words)

                # Collect characters for each word as array
                for word in line.words:
                    characters = [char.value for char in word.characters]
                    print(f"\t\tCharacters for '{word.value}':", characters)

if __name__ == "__main__":
    extract_pdf_text()