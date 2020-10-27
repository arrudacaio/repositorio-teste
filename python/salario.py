nome = input()
salarioFixo = float(input())
valorVenda = float(input())
bonus = valorVenda*0.15
salarioTotal = salarioFixo + bonus
print("salario total = {:.2f}".format(salarioTotal))