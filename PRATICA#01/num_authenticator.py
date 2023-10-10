def num_authenticator(number = int):
    if number > 0:
        return 'P'
    else:
        return 'N'

number = int(input(f"Type a Number: "))
result = num_authenticator(number)

print(f"The Number: {number} is {result}")
