temperatura=int(input('Quanto de graus tá?'))

if temperatura>50:
    print('extremamente quente')

elif 31<=temperatura<=50:
    print('Muito quente')

elif 27<=temperatura<=30:
    print('Tá quente')    

elif 20<=temperatura<=26:
    print('Tá normal')

elif 10<=temperatura<=19:
    print(' Tá frio') 

else: 
    print('Muito frio')