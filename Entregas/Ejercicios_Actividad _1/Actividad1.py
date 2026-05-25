#Codigo Edad Mamá de Juan

edad_Juan = int(input("Ingrese la edad de Juan: "))
edad_Alberto = (2/3)*edad_Juan
edad_Ana = (4/3)*edad_Juan
edad_mama_Juan = edad_Juan + edad_Alberto + edad_Ana

#Por ser edades deben ser convertidos a enteros
edad_Alberto = int(edad_Alberto)
edad_Ana = int(edad_Ana)
edad_mama_Juan = int(edad_mama_Juan)

#Edades
print(f"La edad de Juan es: {edad_Juan}")
print(f"La edad de Alberto es: {edad_Alberto}")
print(f"La edad de Ana es: {edad_Ana}")
print(f"La edad de la mamá de Juan es: {edad_mama_Juan} años")