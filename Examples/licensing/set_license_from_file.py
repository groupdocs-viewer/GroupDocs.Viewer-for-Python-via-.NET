import os
from groupdocs.viewer import License

def set_license_from_file():
    # Get absolute path to license file
    license_path = os.path.abspath("./GroupDocs.Viewer.lic")

    # Check if license file exists
    if not os.path.exists(license_path):
        print(f"License file not found at: {license_path}")
        return

    # Instantiate License and set the license
    license = License()
    license.set_license(license_path)

if __name__ == "__main__":
    set_license_from_file()