from string_ops import *


def test_fix_whitespace():
    assert fix_whitespace("new\nline") == "new line"


def test_fix_hyphenation():
    assert fix_hyphenation("auto- mobile") == "automobile"
