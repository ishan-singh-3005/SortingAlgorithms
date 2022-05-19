def bubble_sort(L: list[int]) -> None:
    """ Sort the items in <L> in non-descending order.
              """

    for iteration in range(len(L)):
        for index in range(len(L) - 1 - iteration):
            if L[index] > L[index + 1]:
                L[index], L[index + 1] = L[index + 1], L[index]
                