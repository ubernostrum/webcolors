"""
Type-hinting stub file for webcolors.py.

This file supports an optional feature of Python 3.5 (and of earlier
Python versions through the mypy-lang project): annotated type
hints. Since the syntax of annotations is not available in Python 2
and since webcolors must support Python 2, the option to specify types
in a .pyi 'stub file' (this file -- similar to a header file in C or
C++) is used.

"""

from typing import Dict, Tuple


def _reversedict(d: Dict) -> Dict:
    pass


def normalize_hex(hex_value: str) -> str:
    pass


def _normalize_integer_rgb(value: int) -> int:
    pass


def normalize_integer_triplet(rgb_triplet: Tuple[int, int, int]) -> Tuple[int, int, int]:
    pass


def _normalize_percent_rgb(value: str) -> str:
    pass


def normalize_percent_triplet(rgb_triplet: Tuple[str, str, str]) -> Tuple[str, str, str]:
    pass


def name_to_hex(name: str, spec: str = u'css3') -> str:
    pass


def name_to_rgb(name: str, spec: str = u'css3') -> Tuple[int, int, int]:
    pass


def name_to_rgb_percent(name: str, spec: str = u'css3') -> Tuple[str, str, str]:
    pass


def hex_to_name(hex_value: str, spec: str = u'css3') -> str:
    pass


def hex_to_rgb(hex_value: str) -> Tuple[int, int, int]:
    pass


def hex_to_rgb_percent(hex_value: str) -> Tuple[str, str, str]:
    pass


def rgb_to_name(rgb_triplet: Tuple[int, int, int], spec: str = u'css3') -> str:
    pass


def rgb_to_hex(rgb_triplet: Tuple[int, int, int]) -> str:
    pass


def rgb_to_rgb_percent(rgb_triplet: Tuple[int, int, int]) -> Tuple[str, str, str]:
    pass


def rgb_percent_to_name(rgb_percent_triplet: Tuple[str, str, str], spec: str = u'css3') -> str:
    pass


def rgb_percent_to_hex(rgb_percent_triplet: Tuple[str, str, str]) -> str:
    pass


def _percent_to_integer(percent: str) -> int:
    pass


def rgb_percent_to_rgb(rgb_percent_triplet: Tuple[str, str, str]) -> Tuple[int, int, int]:
    pass


def html5_parse_simple_color(input: str) -> Tuple[int, int, int]:
    pass


def html5_serialize_simple_color(simple_color: Tuple[int, int, int]) -> str:
    pass


def html5_parse_legacy_color(input: str) -> Tuple[int, int, int]:
    pass
