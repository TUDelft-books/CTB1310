import sympy as sym

h, b , t = sym.symbols('h b t')

b = sym.Integer(300)
h = sym.Integer(400)
t = sym.Integer(12)

b_2 = h / 2 * 3 / 4

Sy = b * t * b / 2 + h/2 / 4 * 5 * t * (b - b_2 / 2) * 2
A = b * t * 3 + h / 2 / 4 * 5 * t * 2

zy = Sy / A

print('zy =', zy)

Izz = t * h **3 / 12 + b * t **3 /12 * 2 + b * t * (h/2)**2 * 2 + t / 4 * 5 * (h/2)**3 / 12 *2 + t * h / 2 /4 *5 * (h/4)**2 * 2
print('Izz =', Izz)
Izz_2 = Izz - b * t **3 /12 * 2
print('Izz_2 =', Izz_2)

Iyy = h * t **3 / 12 + h * t * zy **2 + t * b **3 / 12 * 2 + t * b * (zy - b/2)**2 * 2 + t / 3 * 5 * b_2 **3 * 2 + t * h / 2 / 4 * 5 * (b - b_2/2 - zy)**2 * 2
print('Iyy =', Iyy)
Iyy_2 = Iyy - h * t **3 / 12