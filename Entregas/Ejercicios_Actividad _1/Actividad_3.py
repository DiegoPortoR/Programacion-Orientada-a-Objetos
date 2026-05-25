horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
pago_por_horas_trabajadas = horas_trabajadas*5000
retencion = pago_por_horas_trabajadas*0.125

print(f"Salario bruto: {pago_por_horas_trabajadas}")
print(f"El valor de la retencion en la fuente es: {retencion}")
print(f"El salario neto es de: {pago_por_horas_trabajadas - retencion}")