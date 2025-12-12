import sympy as sym

F, h, b = sym.symbols('F h b')

F = 6000

b = 0.125
h = 0.18

V = F / 2
Izz = b * h**3 / 12
S_a = b * h / 4 * h / 2

print(Izz,S_a)

tau = V * S_a / (Izz * b)
print(tau)