import random

def randomized_quicksort(arr, low, high):
    """
    The main function that implements Randomized Quicksort.
    
    Parameters:
        arr (list): Array to be sorted.
        low (int): Starting index.
        high (int): Ending index.
    """
    if low < high:
        # pi is partitioning index, arr[pi] is now at the right place
        pi = randomized_partition(arr, low, high)

        # Separately sort elements before and after partition
        randomized_quicksort(arr, low, pi-1)
        randomized_quicksort(arr, pi+1, high)

def randomized_partition(arr, low, high):
    """
    Function to pick a random pivot, place the pivot element at its correct
    position in sorted array, and place all smaller (than pivot) to left of pivot and
    all greater elements to right of pivot.
    
    Parameters:
        arr (list): Array to be partitioned.
        low (int): Starting index.
        high (int): Ending index.
    """
    rand_pivot = random.randint(low, high)
    arr[high], arr[rand_pivot] = arr[rand_pivot], arr[high]  # Swap random pivot with last element
    return partition(arr, low, high)

# Example usage:
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
randomized_quicksort(arr, 0, n-1)
print("Sorted array with randomized quicksort is:")
print(arr)
