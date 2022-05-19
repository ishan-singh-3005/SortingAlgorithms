def insert(L: list[int], index: int) -> None:
    """ Insert the item at position <index> in list <L> into the range
                            [0..index] so that [0..index] is in sorted order. [0..index-1]
                            is already sorted.
              """
    while index > 0 and L[index - 1] > L[index]:
        L[index], L[index - 1] = L[index - 1], L[index]
        index -= 1


def insertion_sort(L: list[int]) -> None:
    """ Sort the items in <L> in non-descending order.
              """
    for index in range(len(L)):
        insert(L, index)
