def partition(arr ,low ,high):
    pivot = arr[high]  # pivot
    i = low - 1        # Index of smaller element
    for j in range(low , high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]  # swap
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # swap
    return i + 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[pi] is now at right place
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
arr = list(map(int, input("Enter numbers separated by space: ").strip().split()))
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:", arr)