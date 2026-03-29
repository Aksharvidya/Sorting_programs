def insertion_sort(arr):
    # Loop over the array starting from the second element
    for i in range(1, len(arr)):
        key = arr[i]  # The element to be inserted into the sorted portion
        j = i - 1  # Start comparing with the element before
        
        # Shift elements of arr[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Place the key after the last shifted element
        arr[j + 1] = key
    
    return arr

# Example usage
arr = [12, 11, 13, 5, 6]
print("Sorted array:", insertion_sort(arr))
