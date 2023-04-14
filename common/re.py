import re


def is_match(pattern, str):
    res = re.search(pattern, str)
    return False if not res else True
