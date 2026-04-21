def add(a, b):
    return a + b

def divide (a, b):
    return a / b

# Entrada de datos
print("📌 Calculadora simple")
print("1 - Sumar")
print("2 - Dividir")

opcion = input("Elegí una opción: ")

num1 = float(input("Ingresá el primer número: "))
num2 = float(input("Ingresá el segundo número: "))

if opcion == "1":
    print(f"Resultado: {add(num1, num2)}")
elif opcion == "2":
    try:
        print(f"Resultado: {divide(num1, num2)}")
    except ZeroDivisionError:
        print("❌ No se puede dividir por cero")
else:
    print("❌ Opción inválida")