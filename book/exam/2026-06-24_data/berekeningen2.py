import sympy as sym

h, b , t = sym.symbols('h b t')

h = sym.Integer(300)
b = sym.Integer(400)
t = sym.Integer(12)

F = sym.symbols('F')
F = sym.Integer(54000*5)
print('F =', F)

Iyy = (h * t * (b/2)**2) * 2 + 2 * (t / 3 * 4 * (h/2)**3/ 12 + t / 3 * 4 * (h/2) * (h/4)**2) # ignore h * t **3 / 12 + 
print('Iyy =', Iyy)

S_y_a = t * h * b/2
print('S_y_a =', S_y_a)

tau = F * S_y_a / Iyy / t
print('tau =', tau, 'approx', tau.evalf())

F_2 = tau * t * h / 2
print('F_2 =', F_2, 'approx', F_2.evalf())

a = F_2 * b / F
print('a =', a, 'approx', a.evalf())