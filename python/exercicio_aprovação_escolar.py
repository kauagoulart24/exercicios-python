nota1=float(input('Qual é a sua primeira nota?'))
nota2=float(input('Qual é a sua segunda nota?'))
frequencia=float(input('Qual é a sua frequência?'))
media=(nota1+nota2)/2

if media>=6.5 and frequencia>=75:
    print('Parabéns,você foi aprovado')

elif media>=5 and frequencia>=75:
    print('sorte em,ta de recuperação')

else:
    print('Muito burro, você ta reprovado KKKKKK')