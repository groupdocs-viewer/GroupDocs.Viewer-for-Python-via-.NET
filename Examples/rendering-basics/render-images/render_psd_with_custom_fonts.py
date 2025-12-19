import os
from groupdocs.viewer import Viewer
from groupdocs.viewer.fonts import FolderFontSource, SearchOption, FontSettings
from groupdocs.viewer.options import JpgViewOptions

def render_psd_with_custom_fonts():
    # Create font sources.
    os.makedirs("./custom_fonts_folder", exist_ok=True)
    os.makedirs("./custom_additional_fonts_folder", exist_ok=True)

    # Add custom fonts folder to look for fonts recursively. (look into subfolders too).
    folderFontSource = [FolderFontSource("./custom_fonts_folder", SearchOption.ALL_FOLDERS)]
    # Add custom fonts folder to look for fonts only in this folder (without subfolders).
    additionalFontSource = [FolderFontSource("./custom_additional_fonts_folder", SearchOption.TOP_FOLDER_ONLY)]
    # Call SetFontSources method and supply font sources as arguments.
    FontSettings.set_font_sources(folderFontSource, additionalFontSource)

    # Load PSD file
    with Viewer("sample.psd") as viewer:
        # Create a JPG image.
        viewOptions = JpgViewOptions("render_psd_with_custom_fonts/psd_with_custom_fonts.jpg")
        viewOptions.default_font_name = "Arial"
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_psd_with_custom_fonts()