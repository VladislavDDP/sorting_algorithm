from random import randint

def quick_sort(arr):
    random_number = randint(0, len(arr) - 1)
    left = []
    right = []
    main = arr[random_number]
    return quick_sort(left) + [main] + quick_sort(right)


unsorted = [3, 6, 23, 12, 2, 6, 87]
quick_sort(unsorted)
