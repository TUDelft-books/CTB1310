import sympy as sym
t, F, T, L, d = sym.symbols('t F T L d')	

d = sym.nsimplify(0.25) / sym.sqrt(sym.pi)
t = sym.nsimplify(0.010)
F = 4000
L = 4
T = 12000

sigma = F * L * d / 2 / (sym.pi * (d/2)**3 * t)

I_p = 2 * sym.pi * (d/2)**3 * t

print('I_p =', I_p.evalf()*1e12)

tau = -T * d / 2 / (2 * sym.pi * (d/2)**3 * t)

print('tau =', tau)

A_m = sym.pi * (d/2)**2

print('A_m =', A_m.evalf()*1e6)

tau = T / (2 * A_m * t)

print('tau =', tau.evalf())