import sympy as sym

M_T, R, t = sym.symbols('M_T R t', positive=True)

t = sym.nsimplify(8)
R = sym.nsimplify(90)
M_T = sym.nsimplify(1296000) * 4 * sym.pi
print("M_T =", M_T)

I_p = sym.pi * 2 * R**3 * t

print("I_p =", sym.simplify(I_p),'approx', I_p.evalf())

tau = M_T * R / I_p

print("tau =", sym.simplify(tau), 'approx', tau.evalf())

I_t = sym.pi * 2 * R * t**3 / 3

print("I_t =", sym.simplify(I_t), 'approx', I_t.evalf())
tau_2 = M_T * t/2 / I_t * 2

print("tau_2 =", sym.simplify(tau_2), 'approx', tau_2.evalf())


F, L = sym.symbols('F L', positive=True)

L = 4000

F = M_T / L**2 * 2
print("F =", sym.simplify(F), 'approx', F.evalf())