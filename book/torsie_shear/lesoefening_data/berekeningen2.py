import sympy as sym

t, alpha = sym.symbols('t alpha')
r = sym.symbols('r')
r2 = r + t/2
r1 = r - t/2

theta = sym.symbols('theta')

#zc = sym.sin(alpha)*2 / 3 / alpha * (r2**3 - r1**3) / (r2**2 - r1**2)
#print('zc=',sym.simplify(zc))

r = sym.sqrt(2)*2
t = sym.nsimplify(0.01)
b = sym.nsimplify(4)

z = r * sym.sin(theta)
print(z * t * r)
Sz = sym.integrate(z * t * r, (theta, sym.pi/4, sym.pi/4*3))
print('Sz=',sym.simplify(Sz))
A = t * sym.pi * r * 2 / 4
zc = Sz / (A)
print('zc=',sym.simplify(zc))

Izz = sym.integrate((z - zc)**2 * t * r, (theta, sym.pi/4, sym.pi/4*3))
print('Izz=',sym.simplify(Izz),'approx=',Izz.evalf())

A_tot = A + b * t + t * sym.nsimplify(0.25) * 2
Sz_tot = Sz + b * t * sym.nsimplify(1.75) + t * sym.nsimplify(0.25) * 2 * sym.nsimplify(1.75+0.025/2)
zc_tot = Sz_tot / A_tot
print('zc_tot=',sym.simplify(zc_tot),'approx=',zc_tot.evalf())

Izz = b * t**3 /12 + b * t * (sym.nsimplify(1.75) - zc_tot)**2 + \
       t * sym.nsimplify(0.25) **3 /12 *2 + t * sym.nsimplify(0.25) * 2 * (sym.nsimplify(1.75+0.025/2) - zc_tot)**2 + \
       Izz + A * (zc - zc_tot)**2
print('Izz_tot=',sym.simplify(Izz),'approx=',Izz.evalf())

a = (zc_tot - 2)
print(a.evalf())

import numpy as np

Bv = (12.5*40*20-14.32*15)/25
print('Bv=',Bv)
V_D = 12.5 * 25 - 14.32 - Bv
print('V_D=',V_D)
Mb = 12.5*15*7.5
print('Mb=',Mb)
print('MCA=',12.5*7.5**2/2)
Mc = 12.5*25*12.5-Bv*10
print('Mc=',Mc)
print('MAC=',12.5*20*10-Bv*5)
print('MDB=',Mc/2-1/8*12.5*15**2)

Mtb = Bv*2
Mtc = Mtb+14.32*2
print(Mtb,Mtc)

t = 0.01

Am = np.pi*(2 * np.sqrt(2))**2 / 4 - 2 * np.sqrt(2)*2 * np.sqrt(2)*0.5+0.25*4
tau = Mtc / (2*Am*t*1000)
print('Am=',Am,', tau=',tau)

sigma = Mc * a / Izz * 10000

print('sigma=',sigma.evalf())

Sz = 4 * t * (1.75 - zc_tot) + 0.25 * t * 2 * (1.75 + 0.025/2 - zc_tot)
print('Sz=',Sz.evalf())

tau2 = V_D * 1000 * Sz / Izz / (t * 2)
print('tau2=',tau2.evalf())

tau_tot = tau + tau2/1e6
print('tau_tot=',tau_tot.evalf())
