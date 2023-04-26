total_imoveis = 0


for ano in range(2017, 2023):
    quantidade_imoveis = int(input(f"Digite a quantidade de imóveis no ano {ano}: "))
    total_imoveis += quantidade_imoveis


    print(f"Total de imóveis construídos: {total_imoveis}")