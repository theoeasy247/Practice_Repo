def count_even(numbers):

    count = 0
  
    for num in numbers:
        if num % 2 == 0:
            count = count +1

    return count

numbers = [ 1, 2, 3, 4, 6]
print(count_even(numbers)) 