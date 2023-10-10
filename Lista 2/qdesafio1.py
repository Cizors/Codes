FIBONACCI = [0,1]
NEW_NUMBER = 0
i = 0

print(f"Valor: {FIBONACCI[0]}")
print(f"Valor: {FIBONACCI[1]}")

while NEW_NUMBER <= 501:
    NEW_NUMBER = FIBONACCI[i] + FIBONACCI[i+1]

    FIBONACCI.append(NEW_NUMBER)
    print(f"Valor: {NEW_NUMBER}")

    i += 1
