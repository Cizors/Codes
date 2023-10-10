def number_length(number):
    number_str = str(number)
    length_str = len(number_str)
    return length_str

number = input(f"Type a Number: ")

length = number_length(number)

print(f"Number of Digits: {length}")