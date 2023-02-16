"""
Test accuracy of the mappings of color names and values, by extracting
the definitions of the colors from the relevant standards documents.

"""

import sys
import re
from pathlib import Path
import unittest

import html5lib  # noqa: F401 pylint: disable=unused-import
import requests
from bs4 import BeautifulSoup

thisDir = Path(__file__).parent.absolute()
sys.path.insert(0, str(thisDir.parent))

import webcolors


class HTML4DefinitionTests(unittest.TestCase):
    """
    Extract the names and values of the 16 defined HTML 4 colors from
    the online version of the standard, and check them against this
    module's definitions of them.

    """

    def setUp(self):
        """
        Fetch the HTML 4 color definitions and store them on self.html4_colors.

        """
        self.html4_colors = {}
        soup = BeautifulSoup(
            requests.get("http://www.w3.org/TR/html401/types.html", timeout=5).content,
            "html.parser",
        )
        color_table = soup.find(
            "table", attrs={"summary": "Table of color names and their sRGB values"}
        )
        for cell in color_table.findAll("td"):
            if "width" not in cell.attrs:
                color_name, color_value = cell.text.split(" = ")
                self.html4_colors[color_name] = color_value.replace('"', "").strip()

    def test_color_definitions(self):
        """
        Ensure the values in this module match those in the HTML 4
        specification.

        """
        for color_name, color_value in self.html4_colors.items():
            extracted = webcolors.HTML4_NAMES_TO_HEX[color_name.lower()]
            assert color_value.lower() == extracted


class CSS21DefinitionTests(unittest.TestCase):
    """
    Extract the names and values of the 17 defined CSS 2.1 colors from
    the online version of the standard, and check them against this
    module's definitions of them.

    """

    def setUp(self):
        """
        Fetch the CSS2.1 color definitions and store them on self.css21_colors.

        """
        self.color_matching_re = re.compile(r"^([a-z]+) (#[a-fA-F0-9]{6})$")
        self.css21_colors = {}
        soup = BeautifulSoup(
            requests.get("http://www.w3.org/TR/CSS2/syndata.html", timeout=5).content,
            "html.parser",
        )
        color_table = soup.find("div", attrs={"id": "TanteksColorDiagram20020613"})
        for color_square in color_table.findAll("span", attrs={"class": "colorsquare"}):
            color_name, color_value = self.color_matching_re.search(
                color_square.text
            ).groups()
            self.css21_colors[color_name] = color_value

    def test_color_definitions(self):
        """
        Ensure thie values in this module match those in the
        CSS2.1 specification.

        """
        for color_name, color_value in self.css21_colors.items():
            extracted = webcolors.CSS21_NAMES_TO_HEX[color_name.lower()]
            assert color_value.lower() == extracted


class CSS3DefinitionTests(unittest.TestCase):
    """
    Extract the names and values of the 147 defined CSS 3 colors from
    the online version of the standard, and check them against this
    module's definitions of them.

    """

    def setUp(self):
        """
        Fetch the CSS3 color definitions and store them on self.css3_colors.
        """
        self.css3_colors = {}
        soup = BeautifulSoup(
            requests.get("http://www.w3.org/TR/css3-color/", timeout=5).content,
            "html5lib",
        )
        color_table = soup.findAll("table", attrs={"class": "colortable"})[1]
        color_names = [dfn.text for dfn in color_table.findAll("dfn")]
        hex_values = [
            td.text.strip()
            for td in color_table.findAll(
                "td", attrs={"class": "c", "style": "background:silver"}
            )
            if td.text.startswith("#")
        ]
        rgb_values = [
            td.text.strip()
            for td in color_table.findAll(
                "td", attrs={"class": "c", "style": "background:silver"}
            )
            if not td.text.startswith("#")
            and not td.text.startswith("&")
            and td.text.strip()
        ]
        for i, color_name in enumerate(color_names):
            self.css3_colors[color_name] = {
                "hex": hex_values[i],
                "rgb": tuple(map(int, rgb_values[i].split(","))),
            }

    def test_color_definitions(self):
        """
        Ensure the values in this module match those in the CSS3
        specification.

        """
        for color_name, color_values in self.css3_colors.items():
            extracted_hex = webcolors.CSS3_NAMES_TO_HEX[color_name.lower()]
            extracted_rgb = webcolors.name_to_rgb(color_name)
            assert color_values["hex"].lower() == extracted_hex
            assert color_values["rgb"] == extracted_rgb


if __name__ == "__main__":
    unittest.main()
