"""
Ejercicio 4.6 - Métodos polimórficos

"""


class Profesor:
    """
    Clase padre que representa un profesor de la institución.
    """

    def __init__(self, nombre: str, asignatura: str):
        """
        Inicializa los datos generales del profesor.
        """

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError(
                "El nombre del profesor no puede estar vacío."
            )

        if not isinstance(asignatura, str) or not asignatura.strip():
            raise ValueError(
                "La asignatura no puede estar vacía."
            )

        self.nombre = nombre.strip()
        self.asignatura = asignatura.strip()

    def presentar_perfil(self) -> None:
        """
        Método que presenta la información general del profesor.

        Este método será redefinido en la clase ProfesorTitular.
        """

        print("\nPROFESOR GENERAL")
        print("-" * 55)
        print(f"Nombre     : {self.nombre}")
        print(f"Asignatura : {self.asignatura}")
        print("Vinculación: Docente de la institución")


class ProfesorTitular(Profesor):
    """
    Clase hija que representa un profesor titular.
    """

    def __init__(
        self,
        nombre: str,
        asignatura: str,
        departamento: str,
        anios_titular: int
    ):
        """
        Inicializa los datos de un profesor titular.
        """

        # Invoca el constructor de la clase padre.
        super().__init__(nombre, asignatura)

        if not isinstance(departamento, str) or not departamento.strip():
            raise ValueError(
                "El departamento no puede estar vacío."
            )

        if not isinstance(anios_titular, int):
            raise TypeError(
                "Los años como titular deben ser un número entero."
            )

        if anios_titular < 0:
            raise ValueError(
                "Los años como titular no pueden ser negativos."
            )

        self.departamento = departamento.strip()
        self.anios_titular = anios_titular

    def presentar_perfil(self) -> None:
        """
        Redefine el método heredado de la clase Profesor.

        Este es el método polimórfico del ejercicio.
        """

        print("\nPROFESOR TITULAR")
        print("-" * 55)
        print(f"Nombre       : {self.nombre}")
        print(f"Asignatura   : {self.asignatura}")
        print(f"Departamento : {self.departamento}")
        print("Vinculación  : Profesor titular de planta")

    def mostrar_antiguedad(self) -> None:
        """
        Método exclusivo de la clase ProfesorTitular.
        """

        print(
            f"{self.nombre} lleva {self.anios_titular} "
            "años como profesor titular."
        )


def ejecutar_metodo_polimorfico(docente: Profesor) -> None:
    """
    Recibe una referencia general de tipo Profesor.

    La versión de presentar_perfil() que se ejecuta depende
    del tipo real del objeto recibido.
    """

    print("\n" + "=" * 55)
    print(f"Tipo real del objeto: {type(docente).__name__}")
    print("=" * 55)

    docente.presentar_perfil()


def main() -> None:
    """
    Función principal del programa.
    """

    print("=" * 55)
    print("EJERCICIO 4.6 - MÉTODOS POLIMÓRFICOS")
    print("=" * 55)

    try:
        # Objeto de la clase padre.
        profesor_general = Profesor(
            nombre="Daniel Torres",
            asignatura="Programación orientada a objetos"
        )

        # Objeto de la clase hija.
        profesor_titular = ProfesorTitular(
            nombre="Mariana Cárdenas",
            asignatura="Ingeniería de software",
            departamento="Sistemas e Informática",
            anios_titular=8
        )

        # Referencia anotada como Profesor, pero cuyo objeto real
        # pertenece a ProfesorTitular.
        referencia_profesor: Profesor = profesor_titular

        print("\n1. Método ejecutado sobre un objeto de la clase padre")
        ejecutar_metodo_polimorfico(profesor_general)

        print("\n2. Método ejecutado mediante una referencia general")
        ejecutar_metodo_polimorfico(referencia_profesor)

        print("\n3. Método exclusivo de ProfesorTitular")

        # Se comprueba el tipo real antes de utilizar el método
        # exclusivo de la clase hija.
        if isinstance(referencia_profesor, ProfesorTitular):
            referencia_profesor.mostrar_antiguedad()
        else:
            print(
                "El objeto no es un ProfesorTitular y no tiene "
                "información de antigüedad."
            )

    except (TypeError, ValueError) as error:
        print(f"\nNo fue posible ejecutar el programa: {error}")


if __name__ == "__main__":
    main()