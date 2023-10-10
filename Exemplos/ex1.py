counter = 0
number = 0
average = 0
result = 0

while counter < 3:
    number = input(f"Digite uma nota: ")

    average = int(average) + int(number)
    counter += 1

result = average // 3

print(f"Nota Total: {average}")
print(f"Média: {result}")
