nome_do_aluno = input("Digite o nome do aluno: ")
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

media = (nota_1 + nota_2) /2

print(f"A média do aluno é {media}")

if media >= 7:
    print(f"Aluno(a) {nome_do_aluno} está aprovado")

elif media <6 and media <4:
    print(f"Aluno(a) {nome_do_aluno} está de recuperação")

else:
    print(f"Aluno(a) {nome_do_aluno} está reprovado!")