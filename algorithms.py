def quick_sort(arr):
    left = []
    right = []
    main = 0
    return quick_sort(left) + [main] + quick_sort(right)


unsorted = [3, 6, 23, 12, 2, 6, 87]
quick_sort(unsorted)
