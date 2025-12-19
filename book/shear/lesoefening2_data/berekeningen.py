import sympy as sym

R1, R2= sym.symbols('R1 R2', positive=True)

R1 = sym.nsimplify(300)
R2 = sym.nsimplify(150)
#b1 = sym.nsimplify(300)

A = sym.pi * (R1**2 - R2**2)

print("A=", A, "\approx", A.evalf())

Izz = sym.pi/4 * (R1**4 - R2**4)

print("I_zz=", Izz.simplify(), "\approx", Izz.evalf())

z_snede = sym.nsimplify(250)
Sz = sym.pi * R1 **2 * 4 / (sym.pi * 3) * R1 - sym.pi * R2 **2 * 4 / (sym.pi * 3) * R2

print("Sz=", Sz, "\approx", Sz.evalf())


V = sym.nsimplify(600000)

#tau = V * Sz / (Izz * b2)
#print("tau=", tau.simplify(), "\approx", tau.evalf())
