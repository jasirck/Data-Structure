# Function to generate all possible permutations of a string
def generate_permutations(s):
    def backtrack(path, choices):
        # Base case: If all characters have been used, add the permutation to the result
        if len(path) == len(s):
            permutations.append(''.join(path))
            return
        
        # Recursive case: Explore all possible choices for the next character
        for i in range(len(choices)):
            path.append(choices[i])
            # Recursively call backtrack with the updated path and remaining choices
            backtrack(path, choices[:i] + choices[i+1:])
            # Backtrack by removing the last character to explore other choices
            path.pop()

    permutations = []
    backtrack([], list(s))
    return permutations

# Example usage
input_string = "abc"
result = generate_permutations(input_string)

# Print the result
print("All permutations of the string", input_string, "are:", result)
