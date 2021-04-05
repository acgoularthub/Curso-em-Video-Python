from math import hypot

op = float(input('Insira a medida do cateto oposto: '))
adj = float(input('Insira a medida do cateto adjacente: '))
print('A hipotenusa do cateto oposto de valor {} e o cateto adjacente de valor {} é {:.2f}!'.format(op, adj, hypot(op, adj)))