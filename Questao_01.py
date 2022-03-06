#n = int(input("Número de Entrada: "))
n = 6
i = 1
c = 0
s= str('*')
for i in range(n+1):
  i = (s*c).rjust(i)
  c = c +1
  print(i)
