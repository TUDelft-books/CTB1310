import sympy as sym

M_T, R, t = sym.symbols('M_T R t', positive=True)

I_p = sym.pi * 2 * R**3 * t

print("I_p =", sym.simplify(I_p),'approx', sym.evalf(I_p))

tau = M_T * R / I_p

print("tau =", sym.simplify(tau), 'approx', sym.evalf(tau))

I_t = sym.pi * 2 * R * t**3 / 3

print("I_t =", sym.simplify(I_t), 'approx', sym.evalf(I_t))

tau_2 = M_t * t/2 / I_t * 2
