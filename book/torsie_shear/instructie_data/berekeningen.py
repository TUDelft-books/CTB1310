import sympy as sym

b, h, t = sym.symbols('b h t')

b = sym.nsimplify(500)
h = sym.nsimplify(600)
t = sym.nsimplify(12)

d = sym.sqrt((b/2)**2 + h**2)

A = b * t + 2 * (d * t)
print(f'A = {A}')

NC_z = sym.simplify(d*t*2*h/2 / (d*t*2 + b*t))
print(f'NC_z = {NC_z}')

I_zz = sym.nsimplify(1/12 * b * t**3 + b * t * NC_z**2 + 2 * (1/12 * t*d/h * h**3 + h/h*d * t * (h/2 - NC_z)**2))
print(f'I_zz = {I_zz}')

F, a, L = sym.symbols('F a L')

F = sym.nsimplify(40000*3)
print(f'F = {F} = {F.evalf()} N')

a = sym.nsimplify(600)

L = sym.nsimplify(10000)

S_z_a = b*t*NC_z + 2 * t*d/h * NC_z * NC_z/2
print(f'S_z_a = {S_z_a} = {S_z_a.evalf()} mm^3')

tau_V = sym.simplify(F * S_z_a / I_zz / 2 / t)
print(f'tau_V = {tau_V} = {tau_V.evalf()} MPa')

print(f'M_t = F * a = {F * a} = {(F * a).evalf()} Nmm')

tau_M = F * a / 2 / t / (b * h / 2)
print(f'tau_M = {tau_M} = {tau_M.evalf()} MPa')

sigma_M = F * L * NC_z / I_zz
print(f'sigma_M = {sigma_M} = {sigma_M.evalf()} MPa')

nu = sym.nsimplify(0.3)
E = sym.nsimplify(210000)

