p_de_producao = int(input("Digite o percentual de produção da empresa: "))

if p_de_producao <0:
    print(f"O percentual de crescimento está negativo ({p_de_producao})")

elif p_de_producao == 0:
    print(f"O percentual de produção está neutro ({p_de_producao})")

else:
    print(f"O percentual de crescimento está positivo ({p_de_producao})")