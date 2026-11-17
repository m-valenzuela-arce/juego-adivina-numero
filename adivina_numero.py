import random

print("================================")
print("       ADIVINA EL NUMERO        ")
print("================================")

print("Selecciona la dificultad:")
print("1. Facil (1 a 20)")
print("2. Medio (1 a 50)")
print("3. Dificil (1 a 100)")

dificultad = input("Opcion: ")

if dificultad == "1":
    limite = 20
elif dificultad == "2":
    limite = 50
elif dificultad == "3":
    limite = 100
else:
    print("Opcion no valida. Se usara el nivel medio.")
    limite = 50

numero_secreto = random.randint(1, limite)
max_intentos = 6
intentos = 0
acertado = False

print(f"\nAdivina un numero entre 1 y {limite}.")
print(f"Tienes {max_intentos} intentos.")

while intentos < max_intentos and not acertado:

    entrada = input("\nEscribe un numero: ")

    if not entrada.isdigit():
        print("Debes introducir un numero entero positivo.")
        continue

    numero = int(entrada)

    if numero < 1 or numero > limite:
        print("El numero esta fuera del rango permitido.")
        continue

    intentos += 1

    if numero == numero_secreto:
        acertado = True
        print("\n¡Correcto! Adivinaste el numero.")
        print(f"Lo lograste en {intentos} intentos.")

    elif numero < numero_secreto:
        print("El numero secreto es MAYOR.")
    else:
        print("El numero secreto es MENOR.")

    if not acertado:
        restantes = max_intentos - intentos
        print(f"Intentos restantes: {restantes}")

if not acertado:
    print("\nSe terminaron los intentos.")
    print(f"El numero secreto era {numero_secreto}.")

print("\nFin del juego.")
