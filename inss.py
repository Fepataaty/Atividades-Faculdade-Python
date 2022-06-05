def contribuicaoINSS():
    salario = float(input('Informe o seu salário: '))
    inss = 0
 
    if salario <= 1212:
        inss = salario * 0.075
        print(f'Se o seu salário é de R${salario}, então a porcentagem da sua contribuição é de 7,5%, dando o total de R${inss}. \n')
        repetirOp()
           
    elif salario >= 1213 and salario <= 2427.35:
        inss = salario * 0.09
        print(f'Se o seu salário é de RS${salario}, então a porcentagem da sua contribuição é de 9%, dando o total de R${inss}. \n')
        repetirOp()

    elif salario >= 2427.36 and salario <= 3641.03:
        inss = salario * 0.12
        print(f'Se o seu salário é de RS${salario}, então a porcentagem da sua contribuição é de 12%, dando o total de R${inss}. \n')
        repetirOp()

    elif salario >= 3641.04 and salario <= 7087.22:
        inss = salario * 0.14
        print(f'Se o seu salário é de RS${salario}, então a porcentagem da sua contribuição é de 14%, dando o total de R${inss}. \n')
        repetirOp()

    elif salario >= 7087.23 and salario <= 12136.79:
        inss = salario * 0.145
        print(f'Se o seu salário é de RS${salario}, então a porcentagem da sua contribuição é de 14,5%, dando o total de R${inss}. \n')
        repetirOp()        
            
def repetirOp():
    repetir = int(input('Deseja repetir a operação: \n 1 - Sim \n 2 - Não \n Informe: '))
        
    if repetir == 1:
        contribuicaoINSS()
    elif repetir == 2:
        print('Operação encerrada!')
    else:
        print('Digite uma opção válida')
        repetirOp()

contribuicaoINSS()