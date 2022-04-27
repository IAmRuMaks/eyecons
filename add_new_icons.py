# This script will remove all unnecessary attributes from the svg files
# It will also add fill="currentColor" to the root element

import xml.etree.ElementTree as ElementTree
from os import listdir, makedirs, remove
from os.path import join

ElementTree.register_namespace("", "http://www.w3.org/2000/svg")

INPUT_DIR_NAME = "icons/uncolored"

ALLOWED_ROOT_ATTRIBUTES = ("width", "height", "viewBox")
ALLOWED_PATH_ATTRIBUTES = ("d", "x", "y", "width", "height", "cx", "cy", "rx", "ry", "r", "fill-rule")
ADDITIONAL_ATTRIBUTES = {
    "icons/uncolored": ({"fill": "currentColor"}, {}),
    "icons/black": ({}, {"fill": "#000"}),
    "icons/white": ({}, {"fill": "#fff"})
}


def clean_svg_icon(input_file_path, output_file_path, additional_attributes):
    tree = ElementTree.parse(input_file_path)
    root = tree.getroot()

    attrib_new = {}
    for attribute in root.attrib:
        if attribute in ALLOWED_ROOT_ATTRIBUTES:
            attrib_new[attribute] = root.attrib[attribute]

    for attribute in additional_attributes[0]:
        attrib_new[attribute] = additional_attributes[0][attribute]

    root.attrib = attrib_new

    for child in root:
        attrib_new = {}
        for attribute in child.attrib:
            if attribute in ALLOWED_PATH_ATTRIBUTES:
                attrib_new[attribute] = child.attrib[attribute]

        for attribute in additional_attributes[1]:
            attrib_new[attribute] = additional_attributes[1][attribute]

        child.attrib = attrib_new

    tree.write(output_file_path)


for output_dir in ADDITIONAL_ATTRIBUTES:
    makedirs(output_dir, exist_ok=True)

    for icon_name in listdir(INPUT_DIR_NAME):
        clean_svg_icon(join(INPUT_DIR_NAME, icon_name), join(output_dir, icon_name), ADDITIONAL_ATTRIBUTES[output_dir])

for icon_name in listdir(INPUT_DIR_NAME):
    remove(join(INPUT_DIR_NAME, icon_name))
