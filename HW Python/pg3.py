def find_smallest():
    numbers = [float(input(f"Enter number {i + 1}: ")) for i in range(4)]
    smallest = min(numbers)
    print(f"The smallest number is: {smallest}")
find_smallest()
