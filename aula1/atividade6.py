valor1 = float(input("Digite o valor médio do gol em 2021: "))
valor2 = float(input("Digite o valor médio do gol em 2022: "))
valor3 = float(input("Digite o valor médio do gol no ano atual (2023): "))

if valor1 > valor2 and valor1 > valor3:
    print(f"O maior preço médio do gol foi em 2021 ({valor1})")

elif valor2 > valor1 and valor2 > valor3:
    print(f"O maior preço médio do gol foi em 2022 ({valor2})")

else:
    print(f"O maior preço médio do gol é no ano atual (2023) ({valor3})")


if valor1 < valor2 and valor1 < valor3:
    print(f"O menor preço médio do gol foi em 2021 ({valor1})")

if valor2 < valor1 and valor2 < valor3:
    print(f"O menor preço médio do gol foi em 2022 ({valor2})")

if valor3 < valor1 and valor3 < valor2:
    print(f"O menor preço médio do gol é no ano atual (2023) ({valor3})")
