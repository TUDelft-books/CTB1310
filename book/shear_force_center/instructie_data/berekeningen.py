import sympy as sym

h1, h2, b, t = sym.symbols('h1 h2 b t', positive=True)

t = sym.nsimplify(8)
b = sym.nsimplify(400)
h1 = sym.nsimplify(40)
#h2 = h1 * 4
#b = h1 * 10
h2 = sym.nsimplify(160)

V = sym.nsimplify(25.6*5) * 1000
print('V =', V.evalf(), 'N')

A = (h1 + h2) * t * 2 + b * t

Iyy = (((h1+h2) * t **3) / 12 + (h1+h2) * t * (b/2)**2) * 2 \
    + t * b **3 / 12

Iyy = ((h1+h2) * t * (b/2)**2) * 2 + t * b **3 / 12

print('Iyy =', sym.simplify(Iyy), '=', Iyy.evalf())

Sy1 = t * h1 * b / 2
print('Sy1 =', sym.simplify(Sy1), '=', Sy1.evalf())
sigma_1 = Sy1 / Iyy / t * V

Sy2 = t * h2 * b / 2
sigma_2 = Sy2 / Iyy / t * V

sigma_3 = (Sy1 + Sy2) / Iyy / t * V

Sy3 = Sy1 + Sy2 + b / 2 * b / 4 * t

sigma_4 = Sy3 / Iyy / t * V

print('sigma_1 =', sym.simplify(sigma_1), '=', sigma_1.evalf())
print('sigma_2 =', sym.simplify(sigma_2), '=', sigma_2.evalf())
print('sigma_3 =', sym.simplify(sigma_3), '=', sigma_3.evalf())
print('sigma_4 =', sym.simplify(sigma_4), '=', sigma_4.evalf())

F1 = sigma_1 * t * h1 / 2
F2 = sigma_2 * t * h2 / 2
F3 = sigma_3 * t * b/2 + (sigma_4 - sigma_3) * t * b / 2 * 2 / 3

print('F1 =', sym.simplify(F1), '=', F1.evalf())
print('F2 =', sym.simplify(F2), '=', F2.evalf())
print('F3 =', sym.simplify(F3), '=', F3.evalf())

M = F3 *2 * h2 + F2 * b - F1 * b

print('M =', sym.simplify(M), '=', M.evalf())

a = M / V
print('a =', sym.simplify(a), '=', a.evalf())