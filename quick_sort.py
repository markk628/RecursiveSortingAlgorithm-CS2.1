import time

def partition(items, low, high):
    i = low - 1
    pivot = items[high]

    for index in range(low, high):
        if items[index] <= pivot:
            i += 1
            items[i], items[index] = items[index], items[i]
    
    items[i + 1], items[high] = items[high], items[i + 1]
    return i + 1

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: Θ(n log(n)) Why and under what conditions?
    TODO: Worst case running time: O(n^2) Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort

    """
    if length of items is 1
        return items
    else if low is less than high
        make a variable for partition(items, low, high)
        quick_sort(items, low, part - 1)
        quck_sort(items, part + 1, high)
    """

    if len(items) == 1:
        return items
    elif low < high:
        part = partition(items, low, high)
        quick_sort(items, low, part - 1)
        quick_sort(items, part + 1, high)
        return items

items = [18,24,12,4,9,44,32]
length_of_items = len(items)
start = time.time()
print(quick_sort(items, 0, length_of_items - 1))
end = time.time()
print("%.10f" % (end - start))     