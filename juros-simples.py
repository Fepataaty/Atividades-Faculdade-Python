capital = int(input('Informe o valor do seu capital: '))
taxa = int(input('Informe qual a taxa de porcentagem de juros (em decimal): '))
tempo = int(input('Agora, informe os meses: '))

def jurosSimples():
    juros = capital * taxa * tempo
    print(f'Com um capital de  {capital}, com uma taxa de {taxa} a {tempo} meses, seu juros é de {juros}')

jurosSimples()