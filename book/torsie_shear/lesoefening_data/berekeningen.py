import numpy as np

t = 10e-3
r_outer = 2.8+t/2
r_inner =  2.80 - t/2
A_outer = np.pi*r_outer**2/2
A_inner = np.pi*r_inner**2/2
A_circle = A_outer-A_inner
c_outer = (4*r_outer/(3*np.pi))
c_inner = (4*r_inner/(3*np.pi))
c_1 = (A_outer * c_outer - A_inner * c_inner) / (A_outer - A_inner)
print(c_outer,c_inner,c_1)

Ix_1 = np.pi*r_outer**4/16+A_outer*(c_outer-c_1)**2-(np.pi*r_inner**4/16+A_inner*(c_inner-c_1)**2)
Iy_1 = Ix_1
Ixy_1 = 1/8*r_outer**4+A_outer*(c_outer-c_1)**2-(1/8*r_inner**4+A_inner*(c_inner-c_1)**2)
print(Ix_1,Ixy_1)

Iyy = (Ix_1+Iy_1)/2+(Ix_1-Iy_1)/2*np.cos(2*np.pi/4)+Ixy_1*np.sin(2*np.pi/4)
print(Iyy)
c_2 = 2.8 - c_1*np.sqrt(2)
print('c_2=',c_2)
d = 2.8-2.8/np.sqrt(2)
print('d=',d)
c_4 = 0.25+d-c_2
print('c_4=',c_4)

A_rechthoek = 4*t
A_klein = 0.25*t*2
c_3 = (A_klein*0.125+A_circle*c_4)/(A_rechthoek+A_klein+A_circle)
print('c_3=',c_3)

Iyy_totaal = 1/12*(4*t**3)+A_rechthoek*c_3**2+1/12*(2*t*0.25**3)+A_klein*(c_3-0.125)**2+Iyy+A_circle*(c_4-c_3)**2
print('Iyy_totaal=',Iyy_totaal)

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

Am = np.pi*(2 * np.sqrt(2))**2 / 4 - 2 * np.sqrt(2)*2 * np.sqrt(2)*0.5+0.25*4
tau = Mtc / (2*Am*t*1000)
print('Am=',Am,', tau=',tau)

sigma = Mc * (250+280)/Iyy_totaal / 1e6
print('sigma=',sigma)

import sympy as sym

x = sym.symbols('x')
print(sym.integrate(sym.sin(x)))

t, alpha = sym.symbols('t alpha')
r = sym.symbols('r')
r2 = r + t/2
r1 = r - t/2

theta = sym.symbols('theta')

z = r * sym.sin(theta)
Sz = sym.integrate(z * t * r, (theta, sym.pi/4, sym.pi/4*3))
print('Sz=',sym.simplify(Sz))

A = t * sym.pi * r * 2 / 4
print('A=',sym.simplify(A))

zc_2 = Sz / (A)
print('zc_2=',sym.simplify(zc_2))

Izz = sym.integrate(z**2 * t * r, (theta, sym.pi/4, sym.pi/4*3))
print('Izz=',sym.simplify(Izz))

alpha = sym.pi/4

zc = sym.sin(alpha)*2 / 3 / alpha * (r2**3 - r1**3) / (r2**2 - r1**2)
print('zc=',sym.simplify(zc))

