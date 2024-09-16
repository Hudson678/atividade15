# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.
n1 = float(input("primeiro numero: "))
n2 = float(input("segundo numero: "))

op = input("esoclha uma das operaçoes: soma, subtraçao, multiplicaçao ou divisao: ")
if op == "soma":
    print (n1+n2)
else:
    if op == "subtraçao":
        print (n1-n2)
    elif op == "multiplicaçao":
        print (n1*n2)
    elif op == "divisao":
        print (n1/n2)


   






