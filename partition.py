def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p

    """
    set pivot as last element in items
    for index in range of low to high
        if item at index is less than or equal to the pivot

    """
    i = low - 1
    pivot = items[high]

    for index in range(low, high):
        if items[index] <= pivot:
            i += 1
            items[i], items[index] = items[index], items[i]
    
    items[i + 1], items[high] = items[high], items[i + 1]
    return i + 1