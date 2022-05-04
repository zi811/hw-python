ax = float(input("Координаты точки ax = "))
ay = float(input("Координаты точки ay = "))
bx = float(input("Координаты точки bx = "))
by = float(input("Координаты точки by = "))
k = (ay - by) / (ax - bx)
b = by - k*bx
print("Уравнение прямой, проходящей через эти точки:\n y = %.2f*x + %.2f" % (k, b))