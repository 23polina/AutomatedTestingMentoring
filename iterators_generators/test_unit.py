import pytest

from iterators_generators.task_iterators_generators import merge_elems, map_like


@pytest.mark.parametrize("items, expected",
                         [

                             (([1, 2, 3], 6, 'zhaba', [[1, 2], [3, [2, 6], 4]]),
                             (1, 2, 3, 6, 'z', 'h', 'a', 'b', 'a', 1, 2, 3, 2, 6, 4))

                         ])
def test_merge_elems_mixed_elements(items, expected):
    result = tuple(merge_elems(*items))

    assert result == expected


@pytest.mark.parametrize("items, expected",
                         [
                             ([1, 2, 3], 1),
                             (6, "6:'int' object is not subscriptable"),
                             (True, "True:'bool' object is not subscriptable"),
                             ("zhaba", "z"),

                         ])
def test_map_like_mixed_elements(items, expected):
    result = next(map_like(lambda x: x[0], items))

    assert result == expected
