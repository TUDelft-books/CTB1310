import sympy as sym

h, b , t = sym.symbols('h b t')

b = sym.Integer(300)
h = sym.Integer(400)
t = sym.Integer(12)

F, L = sym.symbols('F L')

F = sym.Integer(4800*9)
print('F =', F)
L = sym.Integer(2000)

b_2 = h / 2 * 3 / 4
print('b_2 =', b_2,'approx', b_2.evalf())

Sy = 2 * b * t * b / 2 + h/2 / 4 * 5 * t * (b - b_2 / 2) * 2
print('Sy =', Sy)
A = b * t * 2 + h / 2 / 4 * 5 * t * 2 + h * t
print('A =', A)

zy = Sy / A

print('zy =', zy)

Izz = t * h **3 / 12 + b * t **3 /12 * 2 + b * t * (h/2)**2 * 2 + t / 4 * 5 * (h/2)**3 / 12 *2 + t * h / 2 /4 *5 * (h/4)**2 * 2
print('Izz =', Izz)
Izz_2 = Izz - b * t **3 /12 * 2
print('Izz_2 =', Izz_2)

Iyy = h * t **3 / 12 + h * t * zy **2 + t * b **3 / 12 * 2 + t * b * (zy - b/2)**2 * 2 + t / 3 * 5 * b_2 **3 * 2 / 12 + t * h / 2 / 4 * 5 * (b - b_2/2 - zy)**2 * 2
print('Iyy =', Iyy)
Iyy_2 = Iyy - h * t **3 / 12
print('Iyy_2 =', Iyy_2)

Sy = h * t * zy + zy * t * zy/2 * 2
print('Sy =', Sy)


V = F
T = F * L

tau = V * Sy / (Iyy * t * 2)
print('tau =', tau, 'approx', tau.evalf())

A_m = b * h - h * b_2 / 2
print('A_m =', A_m)

tau_2 = T / 2 / A_m / t

print('tau_2 =', tau_2, 'approx', tau_2.evalf())