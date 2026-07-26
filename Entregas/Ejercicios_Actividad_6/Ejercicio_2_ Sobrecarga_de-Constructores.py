"""
Ejercicio 2.11 - Sobrecarga de constructores

"""


class ArticuloCientifico:
    """
    Clase que representa los datos principales de un artículo científico.
    """

    def __init__(self, titulo: str, autor: str):
        """
        Primer constructor.

        Inicializa un artículo científico utilizando únicamente
        el título y el autor.
        """

        self._validar_texto(titulo, "título")
        self._validar_texto(autor, "autor")

        self.titulo = titulo.strip()
        self.autor = autor.strip()

        # Valores iniciales para los atributos no recibidos.
        self.palabras_clave = []
        self.publicacion = "Publicación no registrada"
        self.anio = None
        self.resumen = "Resumen no disponible"

    @classmethod
    def crear_con_metadatos(
        cls,
        titulo: str,
        autor: str,
        palabras_clave: list[str],
        publicacion: str,
        anio: int
    ):
        """
        Segundo constructor.

        Inicializa el artículo con título, autor, palabras clave,
        publicación y año.

        Este constructor invoca al primer constructor mediante:
        cls(titulo, autor)
        """

        # Invocación del primer constructor.
        articulo = cls(titulo, autor)

        articulo._validar_palabras_clave(palabras_clave)
        articulo._validar_texto(publicacion, "publicación")
        articulo._validar_anio(anio)

        articulo.palabras_clave = [
            palabra.strip() for palabra in palabras_clave
        ]
        articulo.publicacion = publicacion.strip()
        articulo.anio = anio

        return articulo

    @classmethod
    def crear_completo(
        cls,
        titulo: str,
        autor: str,
        palabras_clave: list[str],
        publicacion: str,
        anio: int,
        resumen: str
    ):
        """
        Tercer constructor.

        Inicializa todos los atributos del artículo científico.

        Este constructor invoca al segundo constructor mediante
        crear_con_metadatos().
        """

        # Invocación del segundo constructor.
        articulo = cls.crear_con_metadatos(
            titulo,
            autor,
            palabras_clave,
            publicacion,
            anio
        )

        articulo._validar_texto(resumen, "resumen")
        articulo.resumen = resumen.strip()

        return articulo

    @staticmethod
    def _validar_texto(valor: str, nombre_campo: str) -> None:
        """
        Verifica que un atributo de texto sea válido.
        """

        if not isinstance(valor, str):
            raise TypeError(
                f"El campo '{nombre_campo}' debe ser una cadena de texto."
            )

        if not valor.strip():
            raise ValueError(
                f"El campo '{nombre_campo}' no puede estar vacío."
            )

    @staticmethod
    def _validar_palabras_clave(palabras_clave: list[str]) -> None:
        """
        Verifica que las palabras clave estén almacenadas en una lista.
        """

        if not isinstance(palabras_clave, list):
            raise TypeError(
                "Las palabras clave deben proporcionarse en una lista."
            )

        if len(palabras_clave) == 0:
            raise ValueError(
                "El artículo debe contener por lo menos una palabra clave."
            )

        for palabra in palabras_clave:
            if not isinstance(palabra, str) or not palabra.strip():
                raise ValueError(
                    "Todas las palabras clave deben ser textos válidos."
                )

    @staticmethod
    def _validar_anio(anio: int) -> None:
        """
        Verifica que el año de publicación sea válido.
        """

        if not isinstance(anio, int):
            raise TypeError("El año de publicación debe ser un número entero.")

        if anio < 1600 or anio > 2100:
            raise ValueError(
                "El año de publicación debe estar entre 1600 y 2100."
            )

    def imprimir_datos(self) -> None:
        """
        Imprime en consola todos los atributos del artículo científico.
        """

        print("\n" + "=" * 68)
        print("ARTÍCULO CIENTÍFICO")
        print("=" * 68)
        print(f"Título      : {self.titulo}")
        print(f"Autor       : {self.autor}")

        if self.palabras_clave:
            palabras = ", ".join(self.palabras_clave)
        else:
            palabras = "No registradas"

        print(f"Palabras clave: {palabras}")
        print(f"Publicación : {self.publicacion}")

        if self.anio is None:
            print("Año         : No registrado")
        else:
            print(f"Año         : {self.anio}")

        print("-" * 68)
        print("Resumen:")
        print(self.resumen)
        print("=" * 68)


def main() -> None:
    """
    Función principal del programa.

    El enunciado solicita utilizar el tercer constructor para crear
    un artículo científico y mostrar sus atributos.
    """

    palabras = [
        "Energías renovables",
        "Sistemas fotovoltaicos",
        "Sostenibilidad",
        "Eficiencia energética"
    ]

    try:
        # Utilización del tercer constructor.
        articulo = ArticuloCientifico.crear_completo(
            titulo=(
                "Optimización de sistemas fotovoltaicos "
                "para comunidades rurales"
            ),
            autor="Laura Fernanda Gómez",
            palabras_clave=palabras,
            publicacion="Revista Colombiana de Energía y Ambiente",
            anio=2025,
            resumen=(
                "El artículo presenta una metodología para dimensionar "
                "sistemas fotovoltaicos destinados a comunidades rurales. "
                "La investigación considera la demanda energética, la "
                "radiación solar disponible y los costos de implementación "
                "para mejorar la confiabilidad y sostenibilidad del sistema."
            )
        )

        articulo.imprimir_datos()

    except (TypeError, ValueError) as error:
        print(f"\nNo fue posible crear el artículo: {error}")


if __name__ == "__main__":
    main()