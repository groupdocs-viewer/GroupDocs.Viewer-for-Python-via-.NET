from groupdocs.viewer import Viewer, FileType
from groupdocs.viewer.options import LoadOptions

def load_xml_document():
    # Method 1: Load XML document by specifying filename with .xml extension
    # GroupDocs.Viewer automatically detects XML format from file extension
    with Viewer("sample.xml") as viewer:
        # Render document
        pass

    # Method 2: Load XML document by explicitly specifying file type in LoadOptions
    # Create load options and set file type to XML
    load_options = LoadOptions()
    load_options.file_type = FileType.XML

    # Load XML document with explicit load options
    with Viewer("sample.xml", load_options) as viewer:
        # Render document
        pass

if __name__ == "__main__":
    load_xml_document()