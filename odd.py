#Python Program to Sort Odd Numbers in the Range Between 0 and 100
def get_odd_numbers_in_range(start, end):
    # Create a list of odd numbers between start and end
    odd_numbers = [num for num in range(start, end + 1) if num % 2 != 0]
    return odd_numbers

def sort_numbers(numbers):
    # Sort the numbers in ascending order
    return sorted(numbers)

# Define the range (0 to 100)
start = 0
end = 100

# Get odd numbers in the given range
odd_numbers = get_odd_numbers_in_range(start, end)

# Sort the odd numbers
sorted_odd_numbers = sort_numbers(odd_numbers)

# Output the sorted list of odd numbers
print("Sorted odd numbers between 0 and 100:", sorted_odd_numbers)
