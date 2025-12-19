from datetime import timedelta
from groupdocs.viewer import Viewer
from groupdocs.viewer.options import HtmlViewOptions

def render_email_with_datetime_format():
    # Load email message
    with Viewer("sample.eml") as viewer:
        # Create an HTML file.
        options = HtmlViewOptions.for_embedded_resources("render_email_with_datetime_format/email_with_datetime_format.html")
        # Apply a custom format to the date in the email message header.
        options.email_options.date_time_format = "MM d yyyy HH:mm tt zzz"
        # Specify the time zone offset. 
        options.email_options.time_zone_offset = timedelta(hours=1)

        viewer.view(options)

if __name__ == "__main__":
    render_email_with_datetime_format()