# Adivina el número

Juego de consola en Python. La computadora elige un número secreto y tú tienes que adivinarlo antes de quedarte sin intentos.

## Cómo se juega

1. Elige un nivel de dificultad:

   | Nivel   | Rango del número |
   |---------|------------------|
   | Fácil   | 1 a 20           |
   | Medio   | 1 a 50           |
   | Difícil | 1 a 100          |

2. Escribe un número. El juego te dice si el número secreto es **MAYOR** o **MENOR**.
3. Tienes **6 intentos** para adivinarlo.

Si escribes algo que no es un número entero positivo, o un número fuera del rango, el juego te avisa y **no te cuenta el intento**.

## Requisitos

- Python 3.6 o más reciente.

## Cómo ejecutarlo

1. Clona el repositorio:

   ```bash
   git clone https://github.com/m-valenzuela-arce/juego-adivina-numero.git
   ```

2. Entra a la carpeta:

   ```bash
   cd juego-adivina-numero
   ```

3. Ejecuta el juego:

   ```bash
   python adivina_numero.py
   ```

   En Mac o Linux puede que tengas que usar `python3` en lugar de `python`.

## Conceptos de programación que usa

- Variables, tipos de datos y operadores
- Entrada y salida de información (`input` y `print`)
- Condiciones `if`, `elif` y `else`
- Ciclos `while`
- Contadores y números aleatorios (`random`)

## Estrategia para jugar 
 
Una buena estrategia es comenzar probando el número 
que se encuentra a la mitad del rango. 
Según la pista MAYOR o MENOR, puedes descartar 
aproximadamente la mitad de los números posibles 
en cada intento. 

Este procedimiento se conoce como búsqueda binaria. 
