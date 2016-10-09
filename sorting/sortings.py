from mpiaa.util import seq_ints, random_ints, powers_of
from mpiaa.timer import time_us


def bubble_sort(items, cmp=lambda x, y: x < y):
    """
    Bubble sort

    :param items: list of items to sort_func
    :param cmp: compare function, cmp(x,y) returns True if x < y, False otherwise
    :return: sorted items
    """
    result = items
    for i in range(len(result)):
        for j in range(0, len(result) - i - 1):
            if cmp(result[j + 1], result[j]):
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def selection_sort(items, cmp=lambda x, y: x < y):
    for i in range(len(items)):
        least = i
        for k in range(i + 1, len(items)):
            if cmp(items[k], items[least]):
                least = k

        items[least], items[i] = items[i], items[least]

    result = items
    # Your code here
    return result


def merge_sort(items, cmp=lambda x, y: x < y):
    """
    Merge sort

    :param items: list of items to sort_func
    :param cmp: compare function, cmp(x,y) returns True if x < y, False otherwise
    :return: sorted items
    """
    if len(items) > 1:
        mid = len(items) // 2
        lefthalf = items[:mid]
        righthalf = items[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if cmp(lefthalf[i], righthalf[j]):
                items[k] = lefthalf[i]
                i = i + 1
            else:
                items[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            items[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            items[k] = righthalf[j]
            j = j + 1
            k = k + 1
    print("Merging ", items)

    result = items
    # Your code here
    return result


def quick_sort(items, cmp=lambda x, y: x < y):
    """
    Quick sort

    :param items: list of items to sort_func
    :param cmp: compare function, cmp(x,y) returns True if x < y, False otherwise
    :return: sorted items
    """
    result = items
    # Your code here
    return result


if __name__ == "__main__":
    time_us({
        "Bubble sort": bubble_sort,
        "Std sort": sorted
    }, ns=powers_of(10, 0, 4), generator=random_ints, repeats=10)
