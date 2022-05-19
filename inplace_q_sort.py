# This version of quicksort mutates the list

def in_place_quicksort(lst):
    _in_place_quicksort(lst, 0, len(lst))


def _in_place_quicksort(lst, start, end):
    if end - start < 2:
        pass
    else:
        pivot_index = _in_place__partition(lst, start, end)
        _in_place_quicksort(lst, start, pivot_index)
        _in_place_quicksort(lst, pivot_index + 1, end)


def _in_place__partition(lst, start, end):
    pivot = lst[start]
    small_i = start + 1
    big_i = end

    while small_i < big_i:
        if lst[small_i] < pivot:
            small_i += 1
        else:
            lst[small_i], lst[big_i - 1] = lst[big_i - 1], lst[small_i]
            big_i -= 1

    lst[start], lst[small_i - 1] = lst[small_i - 1], lst[start]

    return small_i - 1
