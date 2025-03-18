def find_largest_and_smallest(numbers):
    if not numbers:  # Check if the list is empty
        return None, None  # Return None for both values if the list is empty

    largest = max(numbers)
    smallest = min(numbers)
    return largest, smallest

# Example usage:
numbers = [5, 12, 7, 3, 18, 1, 9]
largest, smallest = find_largest_and_smallest(numbers)

print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")
