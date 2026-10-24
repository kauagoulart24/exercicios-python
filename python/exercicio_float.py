produto=input('Qual produto vc quer comprar?')
preço=(float(input('Qual é o preço desse '+ produto +'?')))
unidades=int(input('Quantas unidades vc quer desse produto?'))
s=preço * unidades
print('Você quer comprar um',produto,',mas o preço é',preço,'e quero',unidades,'unidades desse produto.'' Por isso o valor desse produto é {}'.format(s))