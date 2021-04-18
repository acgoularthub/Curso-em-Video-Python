n =int(input('Digite um número inteiro de 0 a 9999: '))

print('No número {} temos:\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(n, n // 1 % 10, n // 10 % 10, n // 100 % 10, n // 1000 % 10))