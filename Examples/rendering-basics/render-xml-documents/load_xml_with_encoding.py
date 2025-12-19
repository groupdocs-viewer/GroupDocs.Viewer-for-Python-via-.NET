from groupdocs.viewer import Viewer, FileType
from groupdocs.viewer.options import LoadOptions

def load_xml_with_encoding():
    # Create load options for XML file type
    load_options = LoadOptions(FileType.XML)
    # Override the encoding specified in XML declaration
    # This allows you to use a different encoding than what's declared in the XML file
    load_options.encoding = "ASCII"

    # Load XML document with custom encoding
    with Viewer("sample.xml", load_options) as viewer:
        # Render document
        pass

if __name__ == "__main__":
    load_xml_with_encoding()