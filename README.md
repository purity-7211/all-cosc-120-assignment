ODD README
# Odd Numbers Sorter

This project contains a Python script that sorts odd numbers in the range between 0 and 100.

## File Structure

- `odd.py`: Contains the main logic for generating and sorting odd numbers within a specified range.

## Usage

To use the script, simply run the `odd.py` file. It will generate a list of odd numbers between 0 and 100, sort them in ascending order, and print the sorted list.

### Example

```python
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
```

### Output

```
Sorted odd numbers between 0 and 100: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
```

## Test Cases

```python
def test_get_odd_numbers_in_range():
    assert get_odd_numbers_in_range(0, 10) == [1, 3, 5, 7, 9]
    assert get_odd_numbers_in_range(10, 20) == [11, 13, 15, 17, 19]
    assert get_odd_numbers_in_range(0, 0) == []
    assert get_odd_numbers_in_range(1, 1) == [1]

def test_sort_numbers():
    assert sort_numbers([5, 3, 1, 9, 7]) == [1, 3, 5, 7, 9]
    assert sort_numbers([11, 9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9, 11]
    assert sort_numbers([]) == []
    assert sort_numbers([1]) == [1]

test_get_odd_numbers_in_range()
test_sort_numbers()
```

## Slicing Using Python Slicing Concepts

### Example

```python
# Define the range (0 to 100)
start = 0
end = 100

# Get odd numbers in the given range
odd_numbers = get_odd_numbers_in_range(start, end)

# Slice the first 10 odd numbers
first_10_odd_numbers = odd_numbers[:10]
print("First 10 odd numbers:", first_10_odd_numbers)

# Slice the last 10 odd numbers
last_10_odd_numbers = odd_numbers[-10:]
print("Last 10 odd numbers:", last_10_odd_numbers)

# Slice odd numbers from index 5 to 15
middle_odd_numbers = odd_numbers[5:16]
print("Odd numbers from index 5 to 15:", middle_odd_numbers)
```

### Output

```
First 10 odd numbers: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
Last 10 odd numbers: [81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
Odd numbers from index 5 to 15: [11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
```

## Algorithm to Compute Factorial Product of Numbers

### Algorithm

1. Define a function `factorial(n)` that takes an integer `n` as input.
2. If `n` is 0 or 1, return 1.
3. Otherwise, return `n * factorial(n-1)`.

### Code

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
print(factorial(5))  # Output: 120
```

### Test Cases

```python
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(7) == 5040
```

## Requirements

- Python 3.x

## Running the Script

To run the script, execute the following command:

```sh
python odd.py
```PERIMETER NAD AREA README
# Area and Perimeter Calculator

This project contains a Python script that calculates the area and perimeter/circumference of different geometric shapes based on user input.

## File Structure

- `area_and_perimeter.py`: Contains the main logic for calculating the area and perimeter/circumference of a circle, triangle, and rectangle.

## Usage

To use the script, simply run the `area_and_perimeter.py` file. It will prompt you to choose a shape and then ask for the necessary dimensions to calculate the area and perimeter/circumference.

### Example

```python
print("choose options a, b or c ")
print("1.area and circumference of a circle")
print("2.area and perimeter of a triangle")
print("3.area and perimeter of a rectangle")
choice = int(input("choose among the choices :"))

from math import pi
if choice == 1:
    radius = float(input("Enter radius of the circle"))
    area = float(pi * radius * radius)
    circumference = float(2 * pi * radius)
    print("area of circle", area)
    print("circumference of circle", circumference)
elif choice == 2:
    base = float(input("Enter base of the triangle"))
    height = float(input("Enter the height of the triangle"))
    hypotenuse = float(input("Enter the hypotenuse of the triangle"))
    area = float(0.5 * base * height)
    perimeter = (base + height + hypotenuse)
    print("area of triangle", area)
    print("perimeter of triangle", perimeter)
elif choice == 3:
    width = float(input("Enter the width of the rectangle"))
    length = float(input("Enter the length of the rectangle"))
    area = float(length * width)
    perimeter = (2 * (length + width))
    print("area of rectangle", area)
    print("perimeter of rectangle", perimeter)
else:
    print("invalid option choose 1, 2 or 3")
```

### Output

The output will vary based on the user's input. Here is an example for a circle with a radius of 5:

```
choose options a, b or c 
1.area and circumference of a circle
2.area and perimeter of a triangle
3.area and perimeter of a rectangle
choose among the choices : 1
Enter radius of the circle: 5
area of circle 78.53981633974483
circumference of circle 31.41592653589793
```

## Test Cases

```python
# No direct test cases as it involves user input
```

## Slicing Using Python Slicing Concepts

### Example

```python
# Define a list of numbers
numbers = list(range(1, 21))

# Slice the first 5 numbers
first_5_numbers = numbers[:5]
print("First 5 numbers:", first_5_numbers)

# Slice the last 5 numbers
last_5_numbers = numbers[-5:]
print("Last 5 numbers:", last_5_numbers)

# Slice numbers from index 5 to 15
middle_numbers = numbers[5:16]
print("Numbers from index 5 to 15:", middle_numbers)
```

### Output

```
First 5 numbers: [1, 2, 3, 4, 5]
Last 5 numbers: [16, 17, 18, 19, 20]
Numbers from index 5 to 15: [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
```

## Algorithm to Compute Factorial Product of Numbers

### Algorithm

1. Define a function `factorial(n)` that takes an integer `n` as input.
2. If `n` is 0 or 1, return 1.
3. Otherwise, return `n * factorial(n-1)`.

### Code

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
print(factorial(5))  # Output: 120
```

### Test Cases

```python
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(7) == 5040
```

## Requirements

- Python 3.x

## Running the Script

To run the script, execute the following command:

```sh
python area_and_perimeter.py
```README OF RECURSION
# Find Largest and Smallest Numbers

This project contains a Python script that finds the largest and smallest numbers in a list.

## File Structure

- `recursion.py`: Contains the main logic for finding the largest and smallest numbers in a list.

## Usage

To use the script, simply run the `recursion.py` file. It will print the largest and smallest numbers from a predefined list.

### Example

```python
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
print(f"The smallest number is: {smallest}")
```

### Output

```
The largest number is: 78
The smallest number is: -12
```

## Test Cases

```python
def test_find_largest_and_smallest():
    assert find_largest_and_smallest([23, 56, 1, 45, 78, 0, -12]) == (78, -12)
    assert find_largest_and_smallest([]) == (None, None)
    assert find_largest_and_smallest([5]) == (5, 5)
    assert find_largest_and_smallest([-1, -2, -3, -4]) == (-1, -4)

test_find_largest_and_smallest()
```

## Slicing Using Python Slicing Concepts

### Example

```python
# Define a list of numbers
numbers = [23, 56, 1, 45, 78, 0, -12]

# Slice the first 3 numbers
first_3_numbers = numbers[:3]
print("First 3 numbers:", first_3_numbers)

# Slice the last 3 numbers
last_3_numbers = numbers[-3:]
print("Last 3 numbers:", last_3_numbers)

# Slice numbers from index 2 to 5
middle_numbers = numbers[2:6]
print("Numbers from index 2 to 5:", middle_numbers)
```

### Output

```
First 3 numbers: [23, 56, 1]
Last 3 numbers: [78, 0, -12]
Numbers from index 2 to 5: [1, 45, 78, 0]
```

## Algorithm to Compute Factorial Product of Numbers

### Algorithm

1. Define a function `factorial(n)` that takes an integer `n` as input.
2. If `n` is 0 or 1, return 1.
3. Otherwise, return `n * factorial(n-1)`.

### Code

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
print(factorial(5))  # Output: 120
```

### Test Cases

```python
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(7) == 5040
```

## Requirements

- Python 3.x

## Running the Script

To run the script, execute the following command:

```sh
python recursion.py
```
