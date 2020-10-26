cont = 0
divisivel = int(input())
quant = int(input())

for i in range(quant):
  num = int(input())
  if num%divisivel == 0:
    cont += 1
  
porcentagem = (cont/quant) * 100

print(f"{cont} ({porcentagem:.1f}%)")