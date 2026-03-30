import sympy as sym

z, r, theta, r1, r2, alpha = sym.symbols('z r theta r1 r2 alpha')

z = sym.sin(theta) * r

integrant = z * r

stap1 = sym.integrate( integrant, (theta, sym.pi/2-alpha, sym.pi/2+alpha) )
stap2 = sym.integrate( stap1, (r, r1, r2) )
print(stap1.simplify())
print(stap2.simplify())

integrant2 = r

stap3 = sym.integrate( integrant2, (theta, sym.pi/2-alpha, sym.pi/2+alpha) )
stap4 = sym.integrate( stap3, (r, r1, r2) )
print(stap3.simplify())
print(stap4.simplify())

print((stap2 / stap4).simplify())