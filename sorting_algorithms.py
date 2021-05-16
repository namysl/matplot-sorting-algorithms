import random


def bubble_sort(array):
    n = len(array)

    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array


def insertion_sort(array):
    n = len(array)

    for i in range(1, n):
        key = array[i]
        j = i - 1

        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key

    return array


def selection_sort(array):
    n = len(array)

    for i in range(n):
        minimum = i
        for j in range(i+1, n):

            if array[minimum] > array[j]:
                minimum = j
        array[i], array[minimum] = array[minimum], array[i]

    return array


def merge_sort(array):

    if len(array) > 1:
        m = len(array) // 2
        left = array[:m]
        right = array[m:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    return array


def quicksort(array):
    smaller = []
    pivot_temp = []
    bigger = []

    if len(array) <= 1:
        return array
    else:
        # pivot = array[0]
        # pivot = random.choice(array)
        pivot = array[len(array)//2]

        for element in array:
            if element < pivot:
                smaller.append(element)
            elif element > pivot:
                bigger.append(element)
            else:
                pivot_temp.append(element)

        left = quicksort(smaller)
        right = quicksort(bigger)

        result = left + pivot_temp + right
        return result
