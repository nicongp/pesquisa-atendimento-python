# Variáveis contadoras
total_excelente = 0
total_ruim = 0
TOTAL_ENTREVISTADOS = 0

numero_pesquisas = int(input('Olá gerente, qual seria o numero de pesquisas que deseja? '))
print('Certo, iniciando pesquisa...')
print(' ')
print('PESQUISA DE SATISFAÇÃO')
print(' ')

# Estrutura de repetição para coletar os dados de cada entrevistado
while TOTAL_ENTREVISTADOS < numero_pesquisas:
    print(f"ENTREVISTA {TOTAL_ENTREVISTADOS + 1}")
    
    # Coleta de dados
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    
    print('Avalie o atendimento prestado:')
    print('1 - EXCELENTE')
    print('2 - BOM')
    print('3 - RUIM')
    
    opiniao = int(input('Digite a sua opinião (1, 2 ou 3): '))
    
    # Estrutura de decisão para verificar a opinião
    if opiniao == 1:
        total_excelente += 1
    elif opiniao == 3:
        total_ruim += 1
    elif opiniao == 2:
        pass 
    else:
        print('Opção inválida! Este voto não será contabilizado nos indicadores principais.')

    TOTAL_ENTREVISTADOS += 1

# Exibição dos resultados finais após o fim do laço de repetição
print(' ')
print('RESULTADO DA PESQUISA')
print(f'Quantidade de respostas "EXCELENTE": {total_excelente}')
print(f'Quantidade de respostas "RUIM": {total_ruim}')
print(' ')