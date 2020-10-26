soma = 0
quant = int(input())

for i in range(quant):
  num = int(input())
  if num%5 == 0:
    soma += num

print(soma)