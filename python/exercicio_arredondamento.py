import math 
n=float(input('Digite um numero:'))
ap=math.ceil(n)
ab=math.floor(n)
print('O numero {} pode arrendodar para {} ou para {}'.format(n,ap,ab))