"""
Calculadora de promedios escolares.
Programa que permite ingresar materias y calificaciones, calcular promedio,
determinar estado (aprobado/reprobado) y encontrar extremos.
"""

from typing import Tuple, List


def ingresar_calificaciones() -> Tuple[List[str], List[float]]:
    """
    Permite al usuario ingresar materias y sus calificaciones.
    Retorna dos listas: una de nombres y otra de calificaciones.
    """
    materias = []
    calificaciones = []

    print("\n=== Ingreso de Calificaciones ===")
    print("Ingrese el nombre de la materia y su calificación (0-10)")

    while True:
        # Solicitar nombre de materia
        nombre = input("\nNombre de la materia (o 'fin' para terminar): ").strip()

        if nombre.lower() == "fin":
            break

        if not nombre:
            print("Error: Debe ingresar un nombre para la materia.")
            continue

        # Solicitar calificación
        while True:
            try:
                calificacion = float(input(f"Calificación para '{nombre}': ").strip())
                if 0 <= calificacion <= 10:
                    break
                else:
                    print("Error: La calificación debe estar entre 0 y 10.")
            except ValueError:
                print("Error: Debe ingresar un número válido.")

        # Almacenar datos
        materias.append(nombre)
        calificaciones.append(calificacion)

        # Preguntar si continuar
        continuar = input("¿Desea agregar otra materia? (s/n): ").strip().lower()
        if continuar != "s" and continuar != "si":
            break

    return materias, calificaciones


def calcular_promedio(calificaciones: List[float]) -> float:
    """
    Calcula el promedio de una lista de calificaciones.
    Retorna 0 si la lista está vacía.
    """
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)


def determinar_estado(calificaciones: List[float], umbral: float = 5.0) -> Tuple[List[int], List[int]]:
    """
    Determina qué materias están aprobadas y reprobadas.
    Retorna dos listas de índices: aprobados y reprobados.
    """
    aprobados = []
    reprobados = []

    for i, calif in enumerate(calificaciones):
        if calif >= umbral:
            aprobados.append(i)
        else:
            reprobados.append(i)

    return aprobados, reprobados


def encontrar_extremos(calificaciones: List[float]) -> Tuple[int, int]:
    """
    Encuentra el índice de la calificación más alta y la más baja.
    Retorna una tupla con (índice_máximo, índice_mínimo).
    """
    if not calificaciones:
        return -1, -1

    indice_max = calificaciones.index(max(calificaciones))
    indice_min = calificaciones.index(min(calificaciones))

    return indice_max, indice_min


def mostrar_resumen(materias: List[str], calificaciones: List[float]) -> None:
    """
    Muestra un resumen completo de todas las materias y estadísticas.
    """
    print("\n" + "=" * 50)
    print("RESUMEN DE CALIFICACIONES")
    print("=" * 50)

    if not materias:
        print("\nNo se ingresaron materias.")
        return

    # Listar todas las materias
    print("\n--- Materias Ingresadas ---")
    for i, (materia, calif) in enumerate(zip(materias, calificaciones), 1):
        print(f"  {i}. {materia}: {calif:.2f}")

    # Calcular promedio
    promedio = calcular_promedio(calificaciones)
    print(f"\n--- Promedio General ---")
    print(f"  Promedio: {promedio:.2f}")

    # Determinar estado
    indice_aprobados, indice_reprobados = determinar_estado(calificaciones)

    print(f"\n--- Materias Aprobadas ({len(indice_aprobados)}) ---")
    if indice_aprobados:
        for i in indice_aprobados:
            print(f"  - {materias[i]}: {calificaciones[i]:.2f}")
    else:
        print("  Ninguna")

    print(f"\n--- Materias Reprobadas ({len(indice_reprobados)}) ---")
    if indice_reprobados:
        for i in indice_reprobados:
            print(f"  - {materias[i]}: {calificaciones[i]:.2f}")
    else:
        print("  Ninguna")

    # Encontrar extremos
    indice_max, indice_min = encontrar_extremos(calificaciones)

    print(f"\n--- Mejor Calificación ---")
    print(f"  {materias[indice_max]}: {calificaciones[indice_max]:.2f}")

    print(f"\n--- Peor Calificación ---")
    print(f"  {materias[indice_min]}: {calificaciones[indice_min]:.2f}")

    print("\n" + "=" * 50)


def main() -> None:
    """Función principal del programa."""
    print("=" * 50)
    print("CALCULADORA DE PROMEDIOS ESCOLARES")
    print("=" * 50)
    print("Ingrese materias y calificaciones (0-10)")
    print("Escriba 'fin' cuando desee terminar\n")

    # Obtener datos del usuario
    materias, calificaciones = ingresar_calificaciones()

    # Mostrar resumen
    mostrar_resumen(materias, calificaciones)

    # Mensaje de despedida
    print("\nGracias por usar la calculadora de promedios.")
    print("¡Hasta luego!")


if __name__ == "__main__":
    main()
