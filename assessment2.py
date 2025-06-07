def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        if x > arr[mid]:
            low = mid + 1
        else:
            upper_bound = arr[mid]
            high = mid - 1

    return iterations, upper_bound

arr = [1.1, 2.5, 3.3, 4.4, 5.8, 7.2]
x = 4.0
iterations, upper_bound = binary_search(arr, x)
print(f"Кількість ітерацій: {iterations}, Верхня межа: {upper_bound}")
