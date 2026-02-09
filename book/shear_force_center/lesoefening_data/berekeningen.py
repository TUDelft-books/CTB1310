import sympy as sym

b = sym.nsimplify(200)
h = sym.nsimplify(400)
t = sym.nsimplify(15)

A = 2 * b * t + h * t * 2
print("Oppervlakte A =", A, "mm²")

Sz = b * t * h + h * t *2 * h / 2

zc = Sz / A

sy = b*t * b / 2 * 2
yc = sy / A

print("NC =", (sym.nsimplify(yc), sym.nsimplify(zc)), "mm")

Izz = (b * t**3) / 12*2 + b * t * (zc)**2 * 2 + (t * 2 * h**3) / 12

Iyy = (t * b**3) / 12 *2 + t * b * (b - yc)**2 *2 + (h * (2 *t)**3) / 12

print("Izz =", sym.nsimplify(Izz), "mm^4")
print("Iyy =", sym.nsimplify(Iyy), "mm^4 approx", Iyy.evalf(), "mm^4")

S_z_1 = b * t * zc
tau_1 = S_z_1 * 100000 / t / Izz
tau_2 = S_z_1 * 100000 / (2 * t) / Izz

S_z_2 = S_z_1 + t * 2 * h/2 * h/4

tau_3 = S_z_2 * 100000 / (2 * t) / Izz

S_z_4 = (b - yc) * t * zc
tau_4 = S_z_4 * 100000 / t / Izz

print('tau_1 =', sym.nsimplify(tau_1), 'MPa', 'approx', tau_1.evalf(), 'MPa')
print('tau_2 =', sym.nsimplify(tau_2), 'MPa', 'approx', tau_2.evalf(), 'MPa')
print('tau_3 =', sym.nsimplify(tau_3), 'MPa', 'approx', tau_3.evalf(), 'MPa')
print('tau_4 =', sym.nsimplify(tau_4), 'MPa', 'approx', tau_4.evalf(), 'MPa')

F_1 = tau_1 * t * b / 2

print('F_1 =', sym.nsimplify(F_1), 'N', 'approx', F_1.evalf(), 'N')

M = F_1 * h

a = M / 100000

print('a =', sym.nsimplify(a), 'mm', 'approx', a.evalf(), 'mm')