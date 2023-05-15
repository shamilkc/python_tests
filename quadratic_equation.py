# ax2 + bx + c = 0, where
# a, b and c are real numbers and
# a ≠ 0

# (-b ± (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

print(x1, x2)


