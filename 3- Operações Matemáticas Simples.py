# Solicita dois números inteiros do usuário e converte para valor absoluto
while True:
	try:
		num1 = abs(int(input("Digite o primeiro número inteiro: ")))
		num2 = abs(int(input("Digite o segundo número inteiro: ")))
		break
	except ValueError:
		print("Por favor, digite apenas números inteiros.")

# Solicita a operação
operacao = input("Escolha a operação (+, -, *, /): ")

# Realiza a operação
if operacao == '+':
	resultado = num1 + num2
elif operacao == '-':
	# Garante resultado positivo na subtração
	resultado = abs(num1 - num2)
elif operacao == '*':
	resultado = num1 * num2
elif operacao == '/':
	if num2 == 0:
		resultado = 'Erro: divisão por zero!'
	else:
		resultado = num1 / num2
else:
	resultado = 'Operação inválida!'

print(f'Resultado: {resultado}')
