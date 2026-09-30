from collections.abc import Iterable


def merge_elems(*elemns):
    for item in elemns:
        if isinstance(item, str):
            yield from item
        elif isinstance(item, Iterable):
            yield from merge_elems(*item)
        else:
            yield item

def map_like(fun, *elems):
    for item in elems:
        try:
            result = fun(item)
            yield result
        except Exception as error:
            yield f"{item}:{error}"
