s = input("Your sequence of numbers: ")
numbers = [int(num) for num in s.split(',')]
numbers.sort()
print('Sorted list:', numbers)
