
def find_smallest(numbers):
    if not numbers:
        return None

    smallest = numbers[0]

    for Num in numbers:
        if Num < smallest:
          smallest = Num

    return smallest

numbers = [56, 90, 34, 21, 25]
print(find_smallest(numbers))
