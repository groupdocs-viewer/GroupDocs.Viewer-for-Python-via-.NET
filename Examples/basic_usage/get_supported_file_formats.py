import aspose.groupdocsviewer as gv

def run():
    supported_file_types = gv.FileType.get_supported_file_types()

    for file_type in sorted(supported_file_types, key=lambda x: x.extension):
        print(file_type)

    print("\nSupported file types retrieved successfully.")
