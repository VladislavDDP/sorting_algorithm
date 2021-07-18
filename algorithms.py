from random import randint
import time

# it is a quick function sort
# @ params: unsorted array
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


# it is a sorting by min element
# @ params: unsorted array
# @ returns sorted array (if works)
def min_element_sort(arr):
    sorted = []

    while len(arr):
        min_element = min(arr)
        sorted.append(min_element)
        arr.remove(min_element)

    return sorted

def testing():
    start = time.perf_counter()
    # declare an unsorted array
    unsorted = [3, 3, 6, 6, 23, 12, 2, 6, 11, 87, 4, 6, 1, 1, 1, 99, 4, 5, 32, 22, 2, 90]
    print(quick_sort(unsorted))
    end = time.perf_counter()

    # RESULT for quick sort
    print(f'Time of quick sort = {end - start:.7f}')

    # test with strings
    unsorted_names = ['Vlad', 'Bob', 'Nikita', 'Lesha', 'Rodik']
    # print(quick_sort(unsorted_names))

    start = time.perf_counter()
    # declare an unsorted array
    unsort = [3, 3, 6, 6, 23, 12, 2, 6, 11, 87, 4, 6, 1, 1, 1, 99, 4, 5, 32, 22, 2, 90]
    print(min_element_sort(unsort))
    end = time.perf_counter()

    # RESULT for min element
    print(f'Time of quick sort = {end - start:.7f}')

    # test with strings
    unsort_names = ['Vlad', 'Bob', 'Nikita', 'Lesha', 'Rodik']
    # print(min_element_sort(unsort_names))


testing()
