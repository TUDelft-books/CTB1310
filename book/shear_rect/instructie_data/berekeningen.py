import sympy as sym
import numpy as np

F, h, b = sym.symbols('F h b')

F = sym.nsimplify(60000)

b = sym.nsimplify(0.125)
h = sym.nsimplify(0.18)

V = F / 2
Izz = b * h**3 / 12
S_a = b * h / 4 * h / 2

print(Izz,S_a)

tau = V * S_a / (Izz * b)
print(tau)


z = sym.symbols('z')
z = sym.nsimplify(.045)

S_a = b * (h/2 - z) * (z + h/2)/2
tau = V * S_a / (Izz * b)
print(tau.simplify())


z = sym.symbols('z')
#z = np.linspace(0,0.09,161)

S_a = b * (h/2 - z) * (z + h/2)/2
tau = V * S_a / (Izz * b)
print(tau)
eq = sym.Eq(sym.nsimplify(380000),tau)
sol = sym.solve(eq,z)
print(sol)
print([s.evalf() for s in sol])
