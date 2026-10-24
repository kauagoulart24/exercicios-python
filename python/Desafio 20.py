import random
alunos=['Kauã','Maria','Ester','Ana']
random.shuffle(alunos)
ordem=', '.join(alunos)
print(f'A ordem de apresentação vai ser por sorteio. A ordem fica desse jeito: {ordem}')