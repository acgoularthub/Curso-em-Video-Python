h = float(input('Digite a altura da parede: '))
l = float(input('Digite a largura da parede: '))
area = h * l
print('Você irá precisar de {:.1f} litros de tinta para pintar esta parede.'.format(area / 2))