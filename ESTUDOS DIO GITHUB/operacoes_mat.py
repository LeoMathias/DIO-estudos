#vamos solicitar como entrada dois numeros e depois vamos realizar uma operação simples entre eles.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

operacao = input("Digite a operação (+, -, *, /): ")
if operacao == "+":
    print(numero1 + numero2)
elif operacao == "-":
    print(numero1 - numero2)
elif operacao == "*":
    print(numero1 * numero2)
elif operacao == "/":
    if numero2 != 0:
        print(numero1 / numero2)
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida.")
