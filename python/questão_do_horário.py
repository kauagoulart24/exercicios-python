horario=float(input('Que horas é?'))

if 6<=horario<12:
    print(' Bom dia!!!!')

elif 12<=horario<18:
    print('Boa tarde!!!')

elif 18<=horario<24:
    print('Boa noite!!!')

else:
    print('Boa madrugada!!!')