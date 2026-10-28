name = "Theoeasy"
language = "Python"
goal = "Softwar Engineer"

print("Name:", name)
print("Language:", language)
print("Goal:", goal)

print("I am learning to become a professional software Engineer" ".")


def find_largest(numbers):
    if not numbers:
        return None

    largest = numbers[0]

    for Num in numbers:
        if Num > largest:
            largest = numbers

    return largest
    numbers = [ 7, 10.4, 39, 21]
    print(find_largest(numbers))




