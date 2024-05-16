s = input("Enter sequence of numbers: ")
numbers = [int(num) for num in s.split(',')]
sorted_unique_numbers = sorted(set(numbers))
print('Sequence of sorted unique numbers:', sorted_unique_numbers)
