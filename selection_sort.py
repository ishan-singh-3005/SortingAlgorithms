def find_min(L: list[int], index: int) -> int:
    """ Return the index of the smallest number in <L>
                            that is at or after position <index>.
              """
    # Alternatively:
    # return L.index(min(L[index:])) + index

    smallest_index = index
    for i in range(index, len(L)):
        if L[smallest_index] > L[i]:
            smallest_index = i
    return smallest_index


def selection_sort(L: list[int]) -> None:
    """ Sort the items in <L> in non-descending order.
              """

    for index in range(len(L) - 1):
        swap_index = find_min(L, index)
        L[index], L[swap_index] = L[swap_index], L[index]
        print("s", L)