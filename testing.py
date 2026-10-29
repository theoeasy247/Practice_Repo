# problem 1 finding largest number in a list of numbers 

def find_largest(numbers):
    if not numbers:
        return None

    largest = numbers[0]

    for Num in numbers:
        if Num > largest:
            largest = Num
    return largest

numbers = [ 4, 6, 8, 23, 47, 10]
print(f"Largest Number is: {find_largest(numbers)}")



# problem 2: finding smaller nubmer in a list of numbers

def find_smallest(numbers):
    if not numbers: 
        return None

    smallest = numbers[0]

    for Num in numbers:
        if Num < smallest:
            smallest = Num

    return smallest
numbers = [50, -2, 45,  50, -1]
print(f"Smallest Number is: {find_smallest(numbers)}")


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
        return None23, 47, 10
    
    smallest = numbers[0]

    for Num in numbers:
        if Num < smallest:
            smallest = Num
    return smallest
numbers = [-9, 45, 2, 44, -17, 90]
print(f"Smallest is  {find_smallest(numbers)}")









def list_sum(numbers):
    total = 0
    
    for num in numbers:
        total =+ num

    return total
numbers = [4, 5, 8, 20, 56]
print(f"Total is: {list_sum(numbers)}")
