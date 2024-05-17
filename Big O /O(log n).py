# Function to perform binary search on a sorted array
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid  # Element found, return its index
        elif mid_val < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return -1  # Element not found

# Example usage
sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target_element = 11

# Perform binary search
index = binary_search(sorted_array, target_element)

# Print the result
if index != -1:
    print("Element", target_element, "found at index:", index)
else:
    print("Element", target_element, "not found in the array.")
