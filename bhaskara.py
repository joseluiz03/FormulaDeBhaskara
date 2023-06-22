print("Fórmula: Δ = Bx² - 4*A*C")
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

delta = b**2 - 4*a*c
print("Valor de Δ =", delta)

if delta >= 0:
    raiz_delta = delta**(1/2)
    valor_x1 = (-b + raiz_delta) / (2*a)
    valor_x2 = (-b - raiz_delta) / (2*a)
    print("Valor de 'x' positivo:", valor_x1, "e valor de 'x' negativo:", valor_x2)
else:
    print("Não existem soluções reais para a equação.")
