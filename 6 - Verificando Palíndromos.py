# Solicita uma palavra ao usuário
palavra = input("Digite uma palavra: ")

# Remove espaços e converte para minúsculas para facilitar a verificação
palavra_formatada = palavra.replace(" ", "").lower()

# Verifica se a palavra é igual à sua versão invertida
if palavra_formatada == palavra_formatada[::-1]:
	print("É um palíndromo!")
else:
	print("Não é um palíndromo.")
