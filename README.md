# 🧮 Calculadora Interactiva de Tablas

Hola 👋 Este es mi proyecto de una calculadora interactiva hecha en Python. Con ella puedo generar tablas de suma, resta, multiplicación y división a partir de un número base y un límite que elige el usuario.

## 📋 Descripción

El programa muestra un menú en pantalla que se repite hasta que el usuario decide salir. Cuando se elige una operación, se pide un número base y un límite, y el programa genera la tabla correspondiente desde el 1 hasta ese límite.

## 🎯 Requerimientos que cumplí

1. **Menú con `while`:** el programa se mantiene en ejecución y muestra las opciones: 1. Suma, 2. Resta, 3. Multiplicación, 4. División y 5. Salir.
2. **Condicionales (`if`, `elif`, `else`):** validan la opción elegida. Si es 5, el programa termina; si es de 1 a 4, se piden los datos; si es otra, se avisa que la opción no existe.
3. **Datos del usuario:** se solicita un número base y un límite numérico para la tabla.
4. **Bucle `for` con `range()`:** recorre desde el 1 hasta el límite, aplica la operación entre el número base y el iterador, y muestra el resultado.

> Tal como se pidió, el código **no utiliza listas ni funciones**.

## ▶️ Cómo ejecutarlo

1. Asegúrate de tener Python 3 instalado.
2. Guarda el archivo `calculadora_tablas.py` en tu computadora.
3. Abre una terminal en la carpeta del archivo y ejecuta:

```bash
python calculadora_tablas.py
```

## 💻 Ejemplo de uso

```
===== MENÚ =====
1. Suma
2. Resta
3. Multiplicación
4. División
5. Salir
¿Qué te gustaría hacer? (1-5): 3
Dime el número base para la tabla: 5
¿Hasta qué número quieres la tabla?: 3

Aquí tienes tu tabla:
5.0 x 1 = 5.0
5.0 x 2 = 10.0
5.0 x 3 = 15.0
```

## 🧠 Lógica del programa

- Uso un `while opcion != 5` para que el menú se repita hasta que el usuario quiera salir.
- Con `if / elif / else` decido qué hacer según la opción elegida.
- Uso `range(1, limite + 1)` para que la tabla incluya el límite indicado, ya que `range()` no toma el último número.
- Como el `for` empieza en 1, nunca ocurre una división entre cero.
- En la división redondeo el resultado a 2 decimales para que se vea ordenado.

## ⚠️ Nota

El programa espera que el usuario escriba números. Si se ingresa texto en lugar de un número, Python mostrará un error, ya que no se pidió usar manejo de excepciones en este ejercicio.

## 📚 Lo que aprendí

Este ejercicio me ayudó a entender cuándo usar `while` (repetir mientras se cumpla una condición) y cuándo usar `for` con `range()` (repetir un número conocido de veces), y cómo combinarlos para crear un programa interactivo.

---

Hecho con dedicación como parte de mi práctica de Python 🐍
