import random

QUICK_COMPARISONS = QUICK_ASSIGNMENTS = 0


def partition(arr, low, high):
    global QUICK_COMPARISONS, QUICK_ASSIGNMENTS
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):
        QUICK_COMPARISONS += 1
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            QUICK_ASSIGNMENTS += 2
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # QUICK_ASSIGNMENTS+=2
    return (i + 1)


# Function to do Quick sort
def quick_sort(arr, low, high):
    global QUICK_COMPARISONS, QUICK_ASSIGNMENTS
    QUICK_COMPARISONS += 1
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def test_quick_sort():
    global QUICK_COMPARISONS, QUICK_ASSIGNMENTS
    for length in [100, 1000, 10000]:
        QUICK_COMPARISONS = QUICK_ASSIGNMENTS = 0
        test_sorted = [i for i in range(length)]
        quick_sort(test_sorted, 0, len(test_sorted) - 1)
        print("Порівняннь у відсортированному за зростанням массиві з %d елементів: %.2f" % (length, QUICK_COMPARISONS))
        print("Копіювань у відсортированному за зростанням массиві з %d elements: %.2f" % (length, QUICK_ASSIGNMENTS))

        QUICK_COMPARISONS = QUICK_ASSIGNMENTS = 0
        test_reversed = [i for i in range(length, 0, -1)]
        quick_sort(test_reversed, 0, len(test_reversed) - 1)
        print("Порівняннь у відсортированному за спаданням массиві з %d елементів: %.2f" % (length, QUICK_COMPARISONS))
        print("Копіювань уу відсортированному за спаданням массиві з %d елементів: %.2f" % (length, QUICK_ASSIGNMENTS))

        QUICK_COMPARISONS = QUICK_ASSIGNMENTS = 0
        for i in range(10):
            test_random = [random.randrange(100) for _ in range(length)]
            quick_sort(test_random, 0, len(test_random) - 1)

        QUICK_COMPARISONS /= 10
        QUICK_ASSIGNMENTS /= 10
        print("Порівняннь у випадково згенерованому массиві з %d елементів: %.2f" % (length, QUICK_COMPARISONS))
        print("Копіювань у випадково згенерованому массиві з %d елементів: %.2f" % (length, QUICK_ASSIGNMENTS))


test_quick_sort()