import sympy as sym

Izz = (sym.nsimplify(4951066*3)+1)/3

V = sym.nsimplify(9900)

tau = V * sym.nsimplify(22050) / Izz / 4
print("tau =", tau.simplify(), "\approx", tau.evalf())