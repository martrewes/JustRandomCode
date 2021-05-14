def productFib(prod):
    a, b = 0, 1
    while prod > a * b:
        a, b = b, a + b     # shift b to a, then add a and b together to create new b
    return [a, b, prod == a * b]

print(productFib(117))