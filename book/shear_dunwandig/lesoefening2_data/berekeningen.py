import sympy as sym

h = sym.nsimplify(300)
b = sym.nsimplify(100)
t = sym.nsimplify(7)

A = b * 3 * t + t * sym.sqrt(h**2+b**2) * 2 + b * t
Sz = t * sym.sqrt(h**2+b**2) * 2 * h / 2 + b * t * h
z_NC = Sz / A

print("Oppervlakte A =", A, "mm², approx. =", A.evalf(), "mm²")
print("Zijzwaartepunt z_NC =", z_NC, "mm, approx. =", z_NC.evalf(), "mm")

I_zz = (b * 3 * t**3) / 12 + b * 3 * t * (z_NC)**2 + 2 * ( t / 3 * sym.sqrt(10) * h**3 / 12 + t * sym.sqrt(h**2+b**2) * (h/2 - z_NC)**2 ) + b * t**3 / 12 + b * t * (h - z_NC)**2
print("Traagheidsmoment I_zz =", I_zz, "mm^4, approx. =", I_zz.evalf(), "mm^4")

V = sym.nsimplify(200000)  # N

S_z_1 = b *3 * t * z_NC
print("Eerste statische moment S_z_1 approx. =", S_z_1.evalf(), "mm³")
tau = V * S_z_1 / (I_zz * t * 2)
print("Schuifspanning tau approx. =", tau.evalf(), "N/mm²")

S_z_2 = b * t * (h - z_NC)
print("Tweede statische moment S_z_2 approx. =", S_z_2.evalf(), "mm³")
tau2 = V * S_z_2 / (I_zz * t * 2)
print("Schuifspanning tau2 approx. =", tau2.evalf(), "N/mm²")

S_z_3 = S_z_1 + t * z_NC / 3 * sym.sqrt(10) * 2 * z_NC / 2
print("Derde statische moment S_z_3 approx. =", S_z_3.evalf(), "mm³")
tau3 = V * S_z_3 / (I_zz * t * 2)
print("Schuifspanning tau3 approx. =", tau3.evalf(), "N/mm²")