p=float(input('Quantas pessoas vão a o churrasco?'))
c=float(input('Quanto cada pessoa vai comer da carne em kg ou g?'))
pc=float(input('Qual é o preço do kg ou g da carne:'))
tc=p*c
tp=pc * tc
print('A quantidade de pessoas é {}. Total de carne é {} e o valor total a pagar por essaa carne é {}'.format(p,tc,tp))