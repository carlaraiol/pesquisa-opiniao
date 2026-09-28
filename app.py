quantidade_excelente = 0
quantidade_ruim = 0

for i in range(50):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade (ex: 10): '))

    opiniao = int(input('Digite sua opinião:\n 1 - Excelente \n 2 - Bom \n 3 - Ruim\n'))

    while opiniao not in [1, 2, 3]:
        print('Opção inválida, digite novamente.')
        opiniao = int(input('Digite sua opinião:\n 1 - Excelente \n 2 - Bom \n 3 - Ruim\n'))
    
    if opiniao == 1:
        quantidade_excelente = quantidade_excelente + 1

    elif opiniao == 3:
        quantidade_ruim = quantidade_ruim + 1

print(f'Quantidade de pessoas que responderam excelente: {quantidade_excelente}')
print(f'Quantidade de pessoas que responderam ruim: {quantidade_ruim}')
