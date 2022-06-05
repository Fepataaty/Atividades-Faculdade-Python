numero = int(input('Digite um número: '))

def tabuada():
	contagem = 0
	controle = 10
	
	while contagem <= controle:
		resultado = numero * contagem
		print(f'{numero} X {contagem} = {resultado}')
		contagem = contagem + 1
tabuada()