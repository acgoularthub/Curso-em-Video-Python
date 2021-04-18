from random import choice
array = []
array.append(input('Insira o nome do primeiro aluno: '))
array.append(input('Insira o nome do segundo aluno: '))
array.append(input('Insira o nome do terceiro aluno: '))
array.append(input('Insira o nome do quarto aluno: '))

print('O aluno que irá apagar o quadro é: {}'.format(choice(array)))