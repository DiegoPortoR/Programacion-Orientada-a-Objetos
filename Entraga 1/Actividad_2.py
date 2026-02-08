suma = 0
x = int(input("ingrese un numero: "))
suma = suma + x
y = int(input("ingrese un numero: "))
x = x + y**2
suma = suma + (x/y)

print(f"El valor de la suma es: {suma}")
