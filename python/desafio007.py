nome=input('Qual é o nome do aluno?')
nota1=int(input('Qual é a primeira nota d(a,o), '+ nome +' dessa disciplina?'))
nota2=int(input('Qual é a segunda nota d(a,o), '+ nome +' dessa disciplina?'))
m=(nota1+nota2)/2
print('A média d(a,o)',nome,'é {}'.format(m))