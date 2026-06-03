import sympy as sym

h, b , t = sym.symbols('h b t')

h = sym.Integer(300)
b = sym.Integer(400)

F, L = sym.symbols('F L')

F = sym.Integer(333000)
#print('F =', F)
L = sym.Integer(2000)

h_2 = b / 2 * 3 / 4
print('h_2 =', h_2,'approx', h_2.evalf())

Sz = h * b * h / 2 - h / 2 * b / 2 * h * 5 / 6
print('Sz =', Sz)
A = h * b - h / 2 * b / 2
print('A =', A)

zc = Sz / A
print('zc =', zc)

h_a = sym.symbols('h_a')
h_a = sym.Integer(50)

S_z_a = h_a * b * (h_a / 2 - zc)
print('S_z_a =', S_z_a)

Izz = b * h **3 / 12 + b * h * (h/2 - zc)**2- (b * (h/2)**3 /36 + b * h / 2 / 2 * (h/6*5 - zc)**2)
print('Izz =', Izz)

tau = F * S_z_a / b / Izz
print('tau =', tau, 'approx', tau.evalf())

