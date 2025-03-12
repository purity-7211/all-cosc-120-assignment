def main():
    # Take user input for starting and ending digits
    start = int(input("Enter the starting digit: "))
    end = int(input("Enter the ending digit: "))

    # Check if start is less than or equal to end
    if start > end:
        print("Starting digit should be less than or equal to ending digit.")
        return

    # Generate list of numbers between start and end (inclusive)
    num_list = list(range(start, end + 1))
    print("Original list:", num_list)

    # Reverse the list using slicing [::-1]
    reversed_list = num_list[::-1]
    print("Reversed list:", reversed_list)

if __name__ == "__main__":
    main()
