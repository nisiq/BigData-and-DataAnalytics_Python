dados2022 = int(input("Digite a quantidade de vendas em 2022: "))
dados2023 = int(input("Digite a quantidade de vendas em 2023: "))

p1 = dados2023-dados2022
p2 = (p1/dados2022)*100

print(f"{p2}%")

if p2 > 20:
    print(f"Variação positiva de {p2}. Bonificação para o time de vendas!!!")

elif p2 >= 2 and p2 <= 20:
    print(f"Variação positiva de {p2}. Pequena bonificação para o time de vendas!")

elif p2 == 2 or p2 > (-10):
    print(f"A variação foi de {p2}. Será necessário um planejamento de políticas de incentivo às vendas.")

else:
    print(f"A variação é preocupante ({p2}). Será necessário o corte de gastos.")



#variação entre 2% e -10%: planejamento de políticas de incentivo ás vendas


#abaixo de -10%: corte de gastos