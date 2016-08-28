def clean_up(s):
    return next(split_into_sentences(fix_hyphenation(fix_whitespace(s))))


def fix_whitespace(s):
    return s.replace("\n", " ")


def fix_hyphenation(s):
    return s.replace("- ", "")


def split_into_sentences(s):
    return map(ensure_ends_with_period, s.split(sep=". "))


def ensure_ends_with_period(s):
    if s.endswith("."):
        return s
    else:
        return s + "."
