def fix_whitespace(s):
    return s.replace("\n", " ")


def fix_hyphenation(s):
    return s.replace("- ", "")


def test_fix_whitespace():
    assert fix_whitespace("new\nline") == "new line"


def test_fix_hyphenation():
    assert fix_hyphenation("auto- mobile") == "automobile"
