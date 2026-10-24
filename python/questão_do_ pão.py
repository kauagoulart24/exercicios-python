preço_do_pão = 6.50
seu_valor = float(input('Quanto de dinheiro você tem?'))
troco=seu_valor-preço_do_pão
if preço_do_pão == seu_valor:
  print('Volte sempre')

elif preço_do_pão < seu_valor:
  print(f'Você comprou o pão. O seu troco é {troco:.2f} reais. Volte sempre.')

else:
  print('Você não tem dinheiro suficiente pra compra o pão')