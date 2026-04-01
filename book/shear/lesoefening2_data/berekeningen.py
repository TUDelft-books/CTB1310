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
Sz = sym.pi * R1 **2 / 2 * 4 / (sym.pi * 3) * R1 - sym.pi * R2 **2 / 2 * 4 / (sym.pi * 3) * R2

alpha = sym.symbols('alpha', positive=True)
#alpha = sym.pi/2
Sz2 = alpha * (R1**2 - R2**2) * 2 * sym.sin(alpha)/3 / (alpha) * (R1**3 - R2**3) / (R1**2 - R2**2)

print("Sz=", Sz, "\approx", Sz.evalf())
print("Sz2=", Sz2.subs(alpha, sym.pi/2), "\approx", Sz2.subs(alpha, sym.pi/2).evalf())


V = sym.nsimplify(270000*15/2)*sym.pi
print("V=", V, "\approx", V.evalf())

tau = V * Sz2 / (Izz * (R1 - R2) * 2)
print("tau=", tau.subs(alpha, sym.pi/2).simplify(), "\approx", tau.subs(alpha, sym.pi/2).evalf())

eq2 = sym.Eq(tau, tau.subs(alpha, sym.pi/2)/2)
sol = sym.solve(eq2, alpha)
print("Oplossing voor alpha:", sol)

print((sol[0]-sym.pi/2).evalf())