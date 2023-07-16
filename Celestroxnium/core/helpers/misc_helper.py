from typing import Iterable, Any


def is_present(substring: str, iterable: Iterable[str]):
    """
    Checks whether a sub-string is present in a list of strings.
    """
    for string in iterable:
        if string is not None and substring in string:
            return True
    
    return False

def set_to_empty(iterable: list[Any]) -> list[Any]:
    """
    Sets an [''] to [] else returns unmodified
    """
    if iterable == ['']:
        iterable = []

    return iterable