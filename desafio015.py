d = int(input('Quantos dias você ficou com o carro: '))
km = float(input("Quantos Km percorridos: "))

tot = (d * 60) + (km * 0.15)

print('Você alugou o carro por {} dia(s), e percorreu {}km'.format(d, km))
print('O total a pagar é: R$ {:.2f}'.format(tot))