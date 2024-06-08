from sympy import symbols, Eq, solve

# Misalnya nilai yang diberikan
p = 12345678901234567890  # nilai contoh
a = 2345678901234567890   # nilai contoh
b = 3456789012345678901   # nilai contoh
x = 4567890123456789012   # nilai contoh

# Persamaan untuk y^2
y = symbols('y')
equation = Eq(y**2, (x**3 + a*x + b) % p)

# Memecahkan untuk y
solutions = solve(equation, y)
print(solutions)
