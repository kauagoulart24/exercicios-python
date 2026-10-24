from math import sqrt ,pow,ceil
numero_do_cateto_oposto=int(input('Digite o numero do cateto oposto:'))
numero_do_cateto_adjacente=int(input('Digite o numero do cateto adjacente:'))
calculo=pow(numero_do_cateto_oposto,2)+pow(numero_do_cateto_adjacente,2)
hipotenusa=sqrt(calculo)
print(f'Pra calcular o resultado da hipotenusa temos que saber o numero do cateto oposto e adjacente,soma e o resultado delas tira a raiz quadrada dela.Vejamos bem: o cateto oposto é {numero_do_cateto_oposto} e o cateto adjacente é {numero_do_cateto_adjacente}. E agora somamos,que da esse numero aqui {calculo:.0f} e por fim saber a hipotenusa, tem que saber a raiz quadrada da soma do cateto oposto elevado a 2 e o adjacente elevado a 2 tambem, soma elas e tirar a raiz que é essa aqui {hipotenusa:.2f}. E é assim achamos o valor da hipotenusa')