points = 0

telephone = input(f"Telefonou para a vítima? ")
local = input(f"Esteve no local do crime? ")
location = input(f"Mora perto da vítima? ")
money = input(f"Devia para a vítima? ")
worked = input(f"Já trabalhou com a vítima? ")

if telephone.lower() == "sim":
    points += 1
if local.lower() == "sim":
    points += 1
if location.lower() == "sim":
    points += 1
if money.lower() == "sim":
    points += 1
if worked.lower() == "sim":
    points += 1

if points == 2:
    print(f"Suspeita")
elif points == 3 or points == 4:
    print(f"Cúmplice")
elif points == 5:
    print(f"Assassino")
else:
    print(f"Inocente")
