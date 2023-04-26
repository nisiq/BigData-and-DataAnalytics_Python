produto1 = float(input("Digite o preço do primeiro produto: "))
produto2 = float(input("Digite o preço do segundo produto: "))
produto3 = float(input("Digite o preço do terceiro produto: "))

if produto1 < produto2 and produto1 < produto3:
    print(f"O primeiro produto é o mais barato ({produto1})")

elif produto2 < produto1 and produto2 < produto3:
    print(f"O produto 2 é o mais barato ({produto2})")

else:
    print(f"O produto 3 é o mais barato ({produto3})")