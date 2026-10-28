def find_largest(numbers):
    if not numbers:
        return None

    largest = numbers [0]

    for Num in numbers:
        if Num > largest:
            largest = Num
        
    return largest
numbers = [56, 90, 478, 67, 12, 10]
print(f"Largest: {find_largest(numbers)}")


def find_smallest(number):
    if not numbers:
        return None
    
    smallest = numbers[0]

    for Num in numbers:
        if Num < smallest:
            smallest = Num
    return smallest
numbers = [-9, 45, 2, 44, -17, 90]
print(f"Smallest is  {find_smallest(numbers)}")

