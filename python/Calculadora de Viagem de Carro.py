v=input('Vocês vão viajar pra onde?')
d=float(input('Qual é a distância em km da viagem de vcs?'))
c=int(input('Qual é o cosumo do carro em km por litro?'))
p=float(input('Qual é o preço do litro da gasolina?'))
csm=d/c
vtg=c
cst_t=(2/csm+vtg)
print('A gente vai viajar para {}. A distância dessa viagem em km é {}. O consumo do carro em km por litros é {:.0f} e o preço da gasolina é {}. E os litros gastos é {:.3f} e o valor total da gasolina é {:.3f},mas eu vou com o meu amigo e vamos dividir os custos, se eu pagasse sozinho ficaria {:.3f}, mas já que vamoos dividir vai ficar pra cada um é {:.3f}'.format(v,d,c,p,csm,vtg,cst_t))