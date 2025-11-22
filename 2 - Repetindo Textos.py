# Solicita a entrada do usuário
texto = input("Digite uma string: ")
while True:
	try:
		vezes = int(input("Digite um número: "))
		break
	except ValueError:
		print("Por favor, digite um número inteiro válido.")

# Exibe a string repetida com espaço entre as repetições
print((texto + ' ') * vezes)
