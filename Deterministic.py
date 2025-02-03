def quicksort(arr, low, high):
    """
    The main function that implements Quicksort.
    
    Parameters:
        arr (list): Array to be sorted.
        low (int): Starting index.
        high (int): Ending index.
    """
    if low < high:
        # pi is partitioning index, arr[pi] is now at right place
        pi = partition(arr, low, high)

        # Separately sort elements before and after partition
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)

def partition(arr, low, high):
    """
    This function takes the last element as pivot, places the pivot element at its correct
    position in sorted array, and places all smaller (than pivot) to left of pivot and
    all greater elements to right of pivot.
    
    Parameters:
        arr (list): Array to be partitioned.
        low (int): Starting index.
        high (int): Ending index.
    """
    pivot = arr[high]  # pivot
    i = low - 1       # Index of smaller element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]  # swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # swap pivot
    return i + 1

# Example usage:
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quicksort(arr, 0, n-1)
print("Sorted array is:")
print(arr)
