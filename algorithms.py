from random import randint

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    random_number = randint(0, len(arr) - 1)
    main = arr[random_number]
    left = [elem for elem in arr if elem != main and elem < main]
    right = [elem for elem in arr if elem != main and elem > main]
    return quick_sort(left) + [main] + quick_sort(right)


unsorted = [3, 3, 6, 6, 23, 12, 2, 6, 87]
print(quick_sort(unsorted))
