# This script will remove all unnecessary attributes from the svg files
# It will also add fill="currentColor" to the root element

import xml.etree.ElementTree as ElementTree
from os import makedirs
from os.path import join

ElementTree.register_namespace("", "http://www.w3.org/2000/svg")

PREVIEW_ICONS_LIST = ("eyecons.svg", "apps.svg", "copy.svg", "file.svg", "folder.svg", "globe.svg", "home.svg",
                      "jigsaw.svg", "symbol_at.svg", "text.svg", "user.svg")

INPUT_DIR_NAME = "icons"
OUTPUT_DIR_NAME_BLACK = "readme_assets/icons_black"
OUTPUT_DIR_NAME_WHITE = "readme_assets/icons_white"

COLOR_BLACK = "black"
COLOR_WHITE = "white"


def recolor_icon(file_path, output_file_path, color):
    tree = ElementTree.parse(file_path)
    root = tree.getroot()

    if "fill" in root.attrib:
        root.attrib.pop("fill")

    for child in root:
        child.attrib["fill"] = color

    tree.write(output_file_path)


makedirs(OUTPUT_DIR_NAME_BLACK, exist_ok=True)
makedirs(OUTPUT_DIR_NAME_WHITE, exist_ok=True)

for path in PREVIEW_ICONS_LIST:
    recolor_icon(join(INPUT_DIR_NAME, path), join(OUTPUT_DIR_NAME_BLACK, path), COLOR_BLACK)
    recolor_icon(join(INPUT_DIR_NAME, path), join(OUTPUT_DIR_NAME_WHITE, path), COLOR_WHITE)
