""" Merge Sort"""


def mergesort(a_list):
    _mergesort(a_list, 0, len(a_list) - 1)


def _mergesort(a_list, first, last):
    # break problem into smaller structurally identical pieces
    mid = (first + last) / 2
    if first < last:
        _mergesort(a_list, first, mid)
        _mergesort(a_list, mid + 1, last)

    # merge solved pieces to get solution to original problem
    a, f, l = 0, first, mid + 1
    tmp = [None] * (last - first + 1)

    while f <= mid and l <= last:
        if a_list[f] < a_list[l]:
            tmp[a] = a_list[f]
            f += 1
        else:
            tmp[a] = a_list[l]
            l += 1
        a += 1

    if f <= mid:
        tmp[a:] = a_list[f:mid + 1]

    if l <= last:
        tmp[a:] = a_list[l:last + 1]

    a = 0
    while first <= last:
        a_list[first] = tmp[a]
        first += 1
        a += 1
