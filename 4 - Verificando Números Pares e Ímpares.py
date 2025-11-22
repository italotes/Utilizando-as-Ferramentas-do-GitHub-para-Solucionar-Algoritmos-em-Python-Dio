# Solicita ao usuário que digite um número inteiro e armazena na variável 'numero'
numero = int(input("Digite um número inteiro: "))

# Usa o operador % para verificar o resto da divisão por 2
if numero % 2 == 0:
    # Se o resto for 0, o número é par
    print("O número é par.")
else:
    # Se não for 0, o número é ímpar
    print("O número é ímpar.")