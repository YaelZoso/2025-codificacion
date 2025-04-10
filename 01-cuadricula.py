import os

ancho = os.get_terminal_size().columns
alto = os.get_terminal_size().lines


def header():
    pre = "contador Izq: 0"
    post = "contador Der: 0"
    print(pre + " " * (ancho - len(pre) - len(post) - 2) + post)


def dibujar_tablero():
    margen_horizontal = 2
    margen_vertical = 6
    ancho_interno = ancho - 2 * margen_horizontal
    alto_interno = alto - margen_vertical

    print(" " * margen_horizontal + "╔" + "═" * (ancho_interno - 2) + "╗")

    for _ in range(alto_interno):
        print(" " * margen_horizontal + "║" + "*" * (ancho_interno - 2) + "║")

    print(" " * margen_horizontal + "╚" + "═" * (ancho_interno - 2) + "╝")


def footer(registros):
    for registro in registros:
        print(registro)


if __name__ == "__main__":
    header()
    dibujar_tablero()
    footer(["registro 1", "registro 2", "registro 3"])
