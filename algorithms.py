from random import randint

# it is a quick function sort
# @ params: unsorted (probably) array
# @ returns sorted array (if works)
def quick_sort(arr):
    # exit way
    if len(arr) < 2:
        return arr
    # basic way
    random_number = randint(0, len(arr) - 1)
    main = arr[random_number]
    arr.remove(main)

    # fill left and right arrays with elements
    left = [elem for elem in arr if elem < main]
    right = [elem for elem in arr if elem >= main]
    return quick_sort(left) + [main] + quick_sort(right)


# declare an unsorted array
unsorted = [3, 3, 6, 6, 23, 12, 2, 6, 11, 87]
print(quick_sort(unsorted))

# test with strings
unsorted_names = ['Vlad', 'Bob', 'Nikita', 'Lesha', 'Rodik']
print(quick_sort(unsorted_names))
