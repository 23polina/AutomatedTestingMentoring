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
                             ((x for x in range(3)), (0, 1, 2)),
                             (((1,),), (1,)),
                             ([],()),
                             ('', ()),
                             ('z', ('z',))
                         ])
def test_merge_elems_edge_cases_elements(items, expected):
    result = tuple(merge_elems(items))

    assert result == expected

def test_merge_elems_no_elements():
    result = tuple(merge_elems())

    assert result == ()


@pytest.mark.parametrize("function, items, expected",
                         [
                             (lambda x: x[0],[1, 2, 3], 1),
                             (lambda x: x[0], 'zhaba', 'z'),
                             (lambda x: x[1], [1, 'd', 3], 'd')

                         ])
def test_map_like_positive_cases_mixed_elements(function, items, expected):
    result = next(map_like(function, items))

    assert result == expected

@pytest.mark.parametrize("function, items, expected",
                         [
                             (lambda x: x[100],[1, 2, 3], "[1, 2, 3]:list index out of range"),
                             (lambda x: x[100], 6, "6:'int' object is not subscriptable"),
                             (lambda x: x[100], True, "True:'bool' object is not subscriptable"),
                             (lambda x: x[100], "zhaba", "zhaba:string index out of range"),
                             (lambda x: x["e"], [1, "d", 23],"[1, 'd', 23]:list indices must be integers or slices, not str")

                         ])
def test_map_like_negative_cases_mixed_elements(function, items, expected):
    result = next(map_like(function, items))

    assert result == expected
