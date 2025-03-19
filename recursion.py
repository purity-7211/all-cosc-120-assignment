def find_largest_and_smallest(numbers):
    if not numbers:
        return None, None  # Handle case for empty list

    largest = max(numbers)
    smallest = min(numbers)

    return largest, smallest

# Example usage
numbers = [23, 56, 1, 45, 78, 0, -12]
largest, smallest = find_largest_and_smallest(numbers)

print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")