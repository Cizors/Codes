valor = 0
desconto = 0
novovalor = 0

valor = input(f"Digite o valor do produto: R$")
desconto = int(valor) * 0.1
novovalor = int(valor) - int(desconto)

print(f"Valor do Produto: R${valor}")
print(f"Valor com Desconto: R${novovalor}")
print(f"Desconto: R${desconto}")