combustível = input("Digite a opção de combustível desejada [ ETANOL | DIESEL | GASOLINA ]: ")
quantidade = int(input("Digite a quantidade (em litros) de gasolina que deseja abastecer o tanque: "))


if combustível == "ETANOL" and quantidade >= 15:
    desconto = 1.70*quantidade*0.04
    vf = (1.70*quantidade)-desconto
    print(f"O desconto é de {desconto}")
    print(f"O valor a ser pago é de {vf}")

elif combustível == "ETANOL" and quantidade < 15:
    desconto = 1.70*quantidade*0.03
    vf = (1.70*quantidade)-desconto
    print(f"O desconto é de {desconto}")
    print(f"O valor a ser pago é de {vf}")


#diesel = 2,00 o litro
else:
    if combustível == "DIESEL" and quantidade >= 15:
        desconto = 2.00*quantidade*0.05
        vf = (2.00*quantidade)-desconto
        print(f"O desconto é de {desconto}")
        print(f"O valor a ser pago é de {vf}")

    elif combustível == "DIESEL" and quantidade < 15:
        desconto = 2.00*quantidade*0.03
        vf = (2.00*quantidade)-desconto
        print(f"O desconto é de {desconto}")
        print(f"O valor a ser pago é de {vf}")
#desconto de 3% o litro
#gasolina 4,99
    else:
        if combustível == "GASOLINA" and quantidade >= 20:
            desconto = 4.99*quantidade*0.03
            vf = (2.00*quantidade)-desconto
            print(f"O desconto é de {desconto}")
            print(f"O valor a ser pago é de {vf}")

        elif combustível == "GASOLINA" and quantidade <20:
            print("sem descontos")