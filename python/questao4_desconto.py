valor_total=float(input('Qual foi o valor total da comprar?'))
if(valor_total>200.00):
    print(f'Compras igual ou maior de 200.00 reais ganha um desconto de 20%. Por isso a sua compra vai sair de {valor_total:.2f} reais para {valor_total-(valor_total*0.20):.2f}, com o desconto aplicado. Volte sempre')
elif(200>=valor_total>=100):
    print(f'Compras entre 100.00 reais à 200.00 reais, ganha um desconto de 10%. Por isso a sua compra vai sair de {valor_total:.2f} para {valor_total-(valor_total*0.10):.2f}, com o desconto aplicado. Volte sempre')
else:
    print('Compras igual ou abaixo de 100.00 reais não ganham desconto')
