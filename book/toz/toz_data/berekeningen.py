import sympy as sym

b, h = sym.symbols('b h')
t = sym.symbols('t')

b = sym.nsimplify(300)
h = sym.nsimplify(300)
t = sym.nsimplify(12) #12

A = b *t + h * t

NC = b * t * b / 2 / A

print('NC =', NC)

Izz = b*t**3/12 + h*t**3 / 12
print('Izz =', Izz)

It = b * t**3 / 3 + h * t**3 / 3
print('It =', It)

q, M_t = sym.symbols('q M_t')
L = sym.symbols('L')

q_random = 2

q = sym.nsimplify(19.2*5*3*q_random / 1000)
print('q =', q, 'approx', q.evalf())

L = sym.nsimplify(2000)

q_random_2 = 3 #3

M_t = sym.nsimplify(288*7*q_random_2 *100)

print('M_t =', M_t, 'approx', M_t.evalf())

q_M_t = q * NC
print('q_M_t=',q_M_t, 'approx', q_M_t.evalf())

M_A = q * NC * L - M_t

print('M_A =', M_A)

tau_wring = M_A * t / 2 / It * 2
print('tau_wring =', tau_wring, 'approx', tau_wring.evalf())

V = q * L

print('V=',V,'approx',V.evalf())

S_z = h / 2 * t * h / 4

tau_shear = V * S_z / Izz / t

print('tau_shear =', tau_shear, 'approx', tau_shear.evalf())