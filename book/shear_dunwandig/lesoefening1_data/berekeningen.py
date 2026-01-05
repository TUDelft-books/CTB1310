import sympy as sym

h = sym.nsimplify(300)
b = sym.nsimplify(300)
t = sym.nsimplify(12)
L = 6
q = sym.nsimplify(24)
#h_A = sym.nsimplify(50)

M =  q * L**2 / 8
V = q * L / 2
print(V)
N = V / 4 * 3
print(N.evalf())
tau = 0
A = b*t+h*t*2
print(A)
zc = h*t*2*h/2 / A
print(zc)
Izz = b * t**3 / 12 + b * t * zc**2 + 2 * t * h**3 / 12 + 2 * t * h * (zc - h/2)**2
print(Izz)
S_a = h * t * (h/2 - zc)
tau = V * (S_a) / t / Izz
sigma = N / A
print('tau, tau, sigma, sigma:')
print(tau)
print(tau.evalf())
print(sigma)
print(sigma.evalf())