def merge_elems(*elemns):
    for item in elemns:
        if hasattr(item, '__iter__') and len(item) > 1:
            yield from merge_elems(*item)
        else:
            yield item


def map_like(fun, *elems):
    for item in elems:
        try:
            result = fun(item)
            yield result
        except TypeError as error:
            yield f"{item}:{error}"
