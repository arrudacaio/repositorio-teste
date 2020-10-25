times = []
gols = []
maior = 0
melhor = [""]
cont = 1

quant = int(input())

for i in range(quant):
  times.append(input())
  gols.append(int(input()))

  if gols[i] > maior:
    cont = 1
    maior = gols[i]
    melhor[0] = times[i]  
  elif gols[i] == maior:
    cont += 1
    melhor.append(times[i]) 

print(f"Time(s) com melhor ataque ({maior} gol(s)): ")

if cont == 1:
  print(melhor[0])
else :
  for i in range(len(melhor)):
    print(melhor[i])

cont = 1
maior = 0
soma = 0

for i in gols:
  soma += i

media = soma/(len(gols))

print(f"\nMédia de gols marcados: {media:.1f} ")