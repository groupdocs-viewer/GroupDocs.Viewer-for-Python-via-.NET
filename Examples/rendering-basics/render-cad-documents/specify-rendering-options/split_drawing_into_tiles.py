from groupdocs.viewer import Viewer
from groupdocs.viewer.options import ViewInfoOptions, HtmlViewOptions, Tile

def split_drawing_into_tiles():
    # Load CAD file
    with Viewer("sample.dwg") as viewer:
        viewInfoOptions = ViewInfoOptions.for_html_view()
        viewInfo = viewer.get_view_info(viewInfoOptions)

        # Get the width and height of the CAD drawing.
        width = viewInfo.pages[0].width
        height = viewInfo.pages[0].height

        # Specify the number of rows and columns to split the drawing into.
        columns = 2
        rows = 2

        # Calculate the width and height of each tile.
        tile_width = width / columns
        tile_height = height / rows
        point_x = 0
        point_y = 0

        # Split the drawing into tiles and convert them to HTML.
        # {0} is replaced with the tile number in the output file name.
        viewOptions = HtmlViewOptions.for_embedded_resources("split_drawing_into_tiles/drawing_into_tiles_{0}.html")
        for i in range(0, columns):
            for j in range(0, rows):
                tile = Tile(point_x + tile_width * i, point_y + tile_height * j, tile_width, tile_height)
                viewOptions.cad_options.tiles.append(tile)
        viewer.view(viewOptions)

if __name__ == "__main__":
    split_drawing_into_tiles()