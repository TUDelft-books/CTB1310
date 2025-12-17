import sympy as sym

h, t, V = sym.symbols('h t V', positive=True)

t = sym.sqrt(2)*20
h = sym.nsimplify(140) #260

V = sym.nsimplify(120000)

A = h * h*2 / 2 - (h - t*sym.sqrt(2)) **2 * 2 / 2

Sz = h ** 2 * 2 / 2 * h / 3 - (h - t*sym.sqrt(2))**2 * 2 / 2 * (h - t*sym.sqrt(2)) / 3

zc = Sz / A

print(zc)
print(zc.evalf())

#sym.plot(zc, (h, 0, 300))

Izz = (h - t * sym.sqrt(2))**3 * t * sym.sqrt(2) * 2 / 12 + t*sym.sqrt(2) * (h - t*sym.sqrt(2)) * (h - t*sym.sqrt(2) - zc) **2 + 2 * t * sym.sqrt(2) * (t*sym.sqrt(2))**3 /36 + t * sym.sqrt(2) * 2 * t * sym.sqrt(2) * (h - t * sym.sqrt(2) / 3 * 2 - zc) **2

print(Izz)
print(Izz.evalf())

h_tau = sym.symbols('h_tau', positive=True)

Sz = (h_tau * sym.sqrt(2) * t) * (zc - h_tau / 2) + (t * sym.sqrt(2) * 2) * t * sym.sqrt(2) / 2 * (zc - t * sym.sqrt(2) / 3 * 2)
print(Sz.subs(h_tau, zc))

tau = V * Sz.subs(h_tau,zc) / Izz / t
print(tau, tau.evalf())

tau = V * Sz.subs(h_tau, 50) / Izz / t
print(tau, tau.evalf())