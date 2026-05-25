import math

radio = int(input("Ingrese el radio del circulo: "))
area_circulo = ((radio)**2)*math.pi
perimetro = 2*math.pi*radio

print(f"El area de la circunferencia es: {area_circulo} y la longitud de la circunferencia es: {perimetro}")
