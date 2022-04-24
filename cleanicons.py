# This script will remove all unnecessary attributes from the svg files
# It will also add fill="currentColor" to the root element

import xml.etree.ElementTree as ElementTree
from os import listdir, makedirs
from os.path import join

ElementTree.register_namespace("", "http://www.w3.org/2000/svg")


INPUT_DIR_NAME = "icons"
OUTPUT_DIR_NAME = "icons_processed"

ALLOWED_ROOT_ATTRIBUTES = ("width", "height", "viewBox")
ALLOWED_PATH_ATTRIBUTES = ("d", "x", "y", "width", "height", "cx", "cy", "rx", "ry", "r", "fill-rule")


def clean_svg_icon(file_path, output_file_path):
    tree = ElementTree.parse(file_path)
    root = tree.getroot()

    attrib_new = {}
    for attribute in root.attrib:
        if attribute in ALLOWED_ROOT_ATTRIBUTES:
            attrib_new[attribute] = root.attrib[attribute]
    root.attrib = attrib_new

    root.attrib["fill"] = "currentColor"

    for child in root:
        attrib_new = {}
        for attribute in child.attrib:
            if attribute in ALLOWED_PATH_ATTRIBUTES:
                attrib_new[attribute] = child.attrib[attribute]
        child.attrib = attrib_new

    tree.write(output_file_path)


makedirs(OUTPUT_DIR_NAME, exist_ok=True)

for path in listdir(INPUT_DIR_NAME):
    clean_svg_icon(join(INPUT_DIR_NAME, path), join(OUTPUT_DIR_NAME, path))
