#AGORA VAMOS SOLICIRAR UMA STRING E UM NUMERO INTEIRO COMO ENTRADA, DEPOIS TEREMOS QUE RETORNAR A STRING REPETIDA O NUMERO DE VEZES INFORMADA

string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))
print(" ".join([string] * numero))