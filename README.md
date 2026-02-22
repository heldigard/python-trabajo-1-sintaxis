# Trabajo 1: Sintaxis Python

## Objetivo
Desarrollar una calculadora de promedios escolares en Python utilizando variables, operadores, estructuras de control y funciones básicas.

## Enunciado
Crear un programa que permita al usuario ingresar nombres de materias y sus calificaciones correspondientes (valores entre 0 y 10).

## Funcionalidades
- Almacenar las materias y calificaciones en listas
- Calcular el promedio general
- Determinar materias aprobadas (>= 5.0) y reprobadas
- Identificar materia con calificación más alta y más baja
- Permitir agregar múltiples materias con opción para finalizar
- Mostrar resumen final completo
- Validación de entradas

## Estructura del código (sin POO)
- `ingresar_calificaciones()` - Permite ingresar materias y calificaciones
- `calcular_promedio(calificaciones)` - Calcula el promedio
- `determinar_estado(calificaciones, umbral)` - Determina aprobados/reprobados
- `encontrar_extremos(calificaciones)` - Encuentra máximo y mínimo
- `main()` - Función principal
- `if __name__ == "__main__":` - Punto de entrada

## Archivos
- `calculadora_promedios.py` - Programa principal

## Uso
```bash
python calculadora_promedios.py
```

## Ejemplo de ejecución
```
==================================================
CALCULADORA DE PROMEDIOS ESCOLARES
==================================================
Ingrese materias y calificaciones (0-10)
Escriba 'fin' cuando desea terminar

Nombre de la materia (o 'fin' para terminar): Matemáticas
Calificación para 'Matemáticas': 8.5
¿Desea agregar otra materia? (s/n): s

Nombre de la materia (o 'fin' para terminar): Historia
Calificación para 'Historia': 4.5
¿Desea agregar otra materia? (s/n): n

==================================================
RESUMEN DE CALIFICACIONES
==================================================

--- Materias Ingresadas ---
  1. Matemáticas: 8.50
  2. Historia: 4.50

--- Promedio General ---
  Promedio: 6.50

--- Materias Aprobadas (1) ---
  - Matemáticas: 8.50

--- Materias Reprobadas (1) ---
  - Historia: 4.50

--- Mejor Calificación ---
  Matemáticas: 8.50

--- Peor Calificación ---
  Historia: 4.50

==================================================

Gracias por usar la calculadora de promedios.
¡Hasta luego!
```
