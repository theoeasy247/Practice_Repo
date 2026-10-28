def find_largest(numbers):
    if not numbers:
        return None

    largest = numbers[0]

    for Num in numbers:
        if Num > largest:
            largest = Num

    return largest
numbers = [7, 10.4, 39, 21]
print(f"Largest number is {find_largest(numbers)}")



