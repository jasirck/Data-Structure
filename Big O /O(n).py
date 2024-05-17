# Function to perform linear search on an array
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Element found, return its index
    return -1  # Element not found

# Example usage
input_array = [3, 7, 1, 9, 4]
target_element = 9

# Perform linear search
index = linear_search(input_array, target_element)

# Print the result
if index != -1:
    print("Element", target_element, "found at index:", index)
else:
    print("Element", target_element, "not found in the array.")
