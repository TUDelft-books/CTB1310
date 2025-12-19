import sympy as sym

b1, b2, h1, h2, h3 = sym.symbols('b1 b2 h1 h2 h3', positive=True)

b1 = sym.nsimplify(300)
h1 = sym.nsimplify(100)
b2 = sym.nsimplify(150)
h2 = sym.nsimplify(50)
h3 = sym.nsimplify(250)

A = b1*h1 + b2 * h3 + (b1 + b2) * h2 / 2

print("A=", A, "\approx", A.evalf())

Sz = b1*h1*h1/2 + (b1 + b2) * h2 / 2 * (h1 + h2/3 * (b1 + 2*b2)/(b1 + b2)) + b2 * h3 * (h1 + h2 + h3/2)

z_bar = Sz / A

print("z_bar=", z_bar.simplify(), "\approx", z_bar.evalf())

Izz = b1*h1**3/12 + b1*h1*(z_bar - h1/2)**2 + \
      b2*h3**3/12 + b1*h1*(z_bar - (h1 + h2 + h3/2))**2 + \
      (b2**2 + 4 * b1 * b2 * b1**2)/(b1 + b2)/36 * h2**3 + (b1 + b2) * h2 / 2 * (z_bar - (h1 + h2/3 * (b1 + 2*b2)/(b1 + b2)))**2

print("I_zz=", Izz.simplify(), "\approx", Izz.evalf())

z_snede = 250
Sz = (h1 + h2 + h3 + z_snede / 2 - z_bar) * (h1 + h2 + h3 - z_snede) * b2

print(Sz)

V = 600000

tau = V * Sz / (Izz * b2)
print("tau=", tau.simplify(), "\approx", tau.evalf())
