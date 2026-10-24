idade = int(input('Qual é a sua idade? '))
condicionamento = input('Você está em bom condicionamento físico? (sim/não) ').lower()
autorizacao = input('Você tem autorização? (sim/não) ').lower()

if 18 <= idade < 35 and (condicionamento == 'sim' or autorizacao == 'sim'):
    print('Você pode participar da olimpiada')

else:
    print('Desculpa, você não pode pasrticipar da olimpiada')