from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_outlook_specific_folder():
    # Load Outlook data file
    with Viewer("sample.pst") as viewer:
        # Create an HTML file.
        viewOptions = HtmlViewOptions.for_embedded_resources("render_outlook_specific_folder/outlook_specific_folder.html")
        # Render messages from the "Inbox" folder and its subfolders.
        viewOptions.outlook_options.folder = "Inbox"
        # Render messages from a specific subfolder in the "Inbox" folder.
        # viewOptions.outlook_options.folder = "Inbox\\Work\\Urgent"
        viewer.view(viewOptions)

if __name__ == "__main__":
    render_outlook_specific_folder()