import math
Va = float(input('Digite o ângulo que você deseja: '))
Vo = math.radians(Va)
Cos = math.cos(Vo)
Se = math.sin(Vo)
Tan = math.tan(Vo)
print('O ângulo de {} tem o SENO de {:.2f}'. format(Va, Se))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(Va, Cos))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(Va, Tan))