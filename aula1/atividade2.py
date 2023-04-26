#portas lógicas > condições
#or = ou | and = e | not inverte
#podemos usar: planilah com conjunto de dados > filtrar valores

t1 = int(input("Digite um número: "))
t2 = int(input("Digite outro número: "))

if t1 > 10 or t2 > 10:
    print("\033[0;37;36mExpressão verdadeira\033[m")
else:
    print("\033[1;95;31mExpressão falsa\033[m")

t1 = int(input("Digite um número: "))
t2 = int(input("Digite outro número: "))

if t1 > 10 and t2 > 10:
    print("\033[0;37;36mExpressão verdadeira\033[m")
else:
    print("\033[1;95;31mExpressão falsa\033[m")