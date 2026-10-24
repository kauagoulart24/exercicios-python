destino=(input('Qual vai ser o destino da viagem?'))
dias=int((input('Quantos dias vai passar nessa viagem?')))
custo=float((input('Qual vai ser o custo por dia dessa viagem?')))
total=custo * dias
print('Então vc vai para',destino,', vai passar',dias,'dias. Por isso o custo em média por dia vai ser',custo,'e o custo total dessa viagem vai ser {}'.format(total))
print(type(destino))