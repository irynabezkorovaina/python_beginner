s = input("Your sequence of characters: ")
sequence = s.split(',')
split = len(sequence)//2
print(sequence[:split], sequence[split:])
