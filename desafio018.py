import math

n = float(input('Digite o ângulo do qual você quer verificar Seno, Cosseno e Tangente: '))
m = math.radians(n)
print('Conseguimos os segintes valores do ângulo de {}°:\nSeno: {:.3f}\nCosseno: {:.3f}\nTangente: {:.3f}\n'.format(n, math.sin(m), math.cos(m), math.tan(m)))
