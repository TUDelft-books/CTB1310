import sympy as sym
import numpy as np

q = sym.symbols('q')
L1, L2, L3 = sym.symbols('L1 L2 L3')

q = sym.nsimplify(20000)
L3 = sym.nsimplify(2)
L2 = sym.nsimplify(5)

VB = q * L3

h, b = sym.symbols('h b')

b = sym.nsimplify(0.010)
h = sym.nsimplify(0.250)

#b = sym.nsimplify(0.125)
#h = sym.nsimplify(0.18)

Izz = b * h**3 / 12
S_a = b * h / 4 * h / 2

print(Izz,S_a)

tau_B = VB * S_a / (Izz * b)
print(tau_B)

Bv = q * (L2 + L3)**2 / 2 / L2
print(Bv)

VB_links = VB - Bv

VS = VB_links + q * L2

print("V_B:", VB)
print("V_B_links:", VB_links)
print("V_S:", VS)

tau_B_links = VB_links * S_a / (Izz * b)
print(tau_B_links)

tau_S = VS * S_a / (Izz * b)
print(tau_S)