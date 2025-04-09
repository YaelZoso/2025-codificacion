import os


def dibujar_cuadricula():
    size = os.get_terminal_size()
    ancho = size.columns
    alto = size.lines

    margen_horizontal = 2
    margen_vertical = 6
    ancho_interno = ancho - 2 * margen_horizontal
    alto_interno = alto - margen_vertical

    print("Contador Izq: 0".ljust(ancho // 2) + "Contador Der:0".rjust(ancho // 2))

    print(" " * margen_horizontal + "┌" + "─" * (ancho_interno - 2) + "┐")

    for _ in range(alto_interno):
        print(" " * margen_horizontal + "│" + "*" * (ancho_interno - 2) + "│")

    print(" " * margen_horizontal + "└" + "─" * (ancho_interno - 2) + "┘")

    print("\nRegistro 1:")
    print("Registro 2:")
    print("Registro 3:")


if __name__ == "__main__":
    dibujar_cuadricula()
