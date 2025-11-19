import math  # noqa: INP001

# Cantidad de microsegundos que hay en un segundo
UN_SEGUNDO = 10**6

datos = [
    {
        "limite_inferior": 1 * (10**3),
        "limite_superior": 1 * (10**6),
        "microsegundos": UN_SEGUNDO,
        "cant_tiempo_legible": "1 segundo",
    },
    {
        "limite_inferior": 7.746 * (10**3),
        "limite_superior": 6 * (10**7),
        "microsegundos": 60 * UN_SEGUNDO,
        "cant_tiempo_legible": "1 minuto",
    },
    {
        "limite_inferior": 6 * (10**4),
        "limite_superior": 3.6 * (10**9),
        "microsegundos": 3600 * UN_SEGUNDO,
        "cant_tiempo_legible": "1 hora",
    },
    {
        "limite_inferior": 2.9393 * (10**5),
        "limite_superior": 8.64 * (10**10),
        "microsegundos": 24 * 3600 * UN_SEGUNDO,
        "cant_tiempo_legible": "1 día",
    },
    {
        "limite_inferior": 1.61046 * (10**6),
        "limite_superior": 2.592 * (10**12),
        "microsegundos": 30 * 24 * 3600 * UN_SEGUNDO,
        "cant_tiempo_legible": "1 mes",
    },
    {
        "limite_inferior": 5.5757 * (10**6),
        "limite_superior": 3.1104 * (10**13),
        "microsegundos": 12 * 30 * 24 * 3600 * UN_SEGUNDO,
        "cant_tiempo_legible": "1 año",
    },
    {
        "limite_inferior": 5.5757 * (10**7),
        "limite_superior": 3.1104 * (10**15),
        "microsegundos": 100 * 12 * 30 * 24 * 3600 * UN_SEGUNDO,
        "cant_tiempo_legible": "1 siglo",
    },
]


def f(n: float, microsegundos: float) -> float:
    """
    Función que representa la ecuación n * log2(n) - microsegundos.
    """
    return n * math.log2(n) - microsegundos


def encontrar_n_entre_rangos(a: float, b: float, microsegundos: float) -> float:
    """
    Encuentra el valor de n, sabiendo que n está entre a y b,
    de la función: n * log_2(n) = microsegundos.
    """
    limite_inferior, limite_superior = a, b

    for _ in range(100):
        mitad = (limite_inferior + limite_superior) / 2
        if f(mitad, microsegundos) == 0:
            return mitad
        if f(mitad, microsegundos) > 0:
            limite_superior = mitad
        else:
            limite_inferior = mitad

    return (limite_inferior + limite_superior) / 2


def convertir_a_notacion_cientifica(numero: float) -> str:
    """
    Convierte un número a notación científica (por ejemplo 5.26 * 10^13).
    """
    exponente = math.floor(math.log10(abs(numero)))
    coeficiente = numero / (10**exponente)
    return f"{coeficiente:.3f} * 10^{exponente}"


def main() -> None:  # noqa: D103
    for dato in datos:
        n = encontrar_n_entre_rangos(
            dato["limite_inferior"],
            dato["limite_superior"],
            dato["microsegundos"],
        )
        limite_inferior_cientifico = convertir_a_notacion_cientifica(
            dato["limite_inferior"],
        )
        limite_superior_cientifico = convertir_a_notacion_cientifica(
            dato["limite_superior"],
        )
        n_cientifico = convertir_a_notacion_cientifica(n)

        print(f"Valor de n para {dato['cant_tiempo_legible']}:")
        print(
            f"    Está entre {limite_inferior_cientifico} y {limite_superior_cientifico}",  # noqa: E501
        )
        print(f"    Y su valor aproximado es: {n_cientifico}\n")


if __name__ == "__main__":
    main()
