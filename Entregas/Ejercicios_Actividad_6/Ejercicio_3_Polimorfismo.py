"""
Ejercicio 4.4 - Polimorfismo

"""


class Profesor:
    """
    Clase padre que representa un profesor genérico.
    """

    def __init__(self, nombre: str, departamento: str):
        """
        Inicializa los datos generales de un profesor.
        """

        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre del profesor no puede estar vacío.")

        if not isinstance(departamento, str) or not departamento.strip():
            raise ValueError("El departamento no puede estar vacío.")

        self.nombre = nombre.strip()
        self.departamento = departamento.strip()

    def mostrar_informacion(self) -> None:
        """
        Muestra la información de un profesor general.

        Este método será sobrescrito en la clase ProfesorTitular.
        """

        print("\n" + "=" * 62)
        print("PROFESOR")
        print("=" * 62)
        print(f"Nombre       : {self.nombre}")
        print(f"Departamento : {self.departamento}")
        print("Categoría    : Profesor general")
        print("=" * 62)


class ProfesorTitular(Profesor):
    """
    Clase hija que representa un profesor titular.
    """

    def __init__(
        self,
        nombre: str,
        departamento: str,
        especialidad: str,
        anios_experiencia: int
    ):
        """
        Inicializa los datos del profesor titular.
        """

        # Invocación del constructor de la clase padre.
        super().__init__(nombre, departamento)

        if not isinstance(especialidad, str) or not especialidad.strip():
            raise ValueError("La especialidad no puede estar vacía.")

        if not isinstance(anios_experiencia, int):
            raise TypeError("Los años de experiencia deben ser un entero.")

        if anios_experiencia < 0:
            raise ValueError(
                "Los años de experiencia no pueden ser negativos."
            )

        self.especialidad = especialidad.strip()
        self.anios_experiencia = anios_experiencia

    def mostrar_informacion(self) -> None:
        """
        Sobrescribe el método definido en la clase Profesor.

        Python selecciona esta versión cuando el objeto real
        pertenece a la clase ProfesorTitular.
        """

        print("\n" + "=" * 62)
        print("PROFESOR TITULAR")
        print("=" * 62)
        print(f"Nombre             : {self.nombre}")
        print(f"Departamento       : {self.departamento}")
        print(f"Especialidad       : {self.especialidad}")
        print(f"Años de experiencia: {self.anios_experiencia}")
        print("Categoría          : Profesor titular")
        print("=" * 62)


def presentar_profesor(profesor: Profesor) -> None:
    """
    Recibe una referencia de tipo Profesor.

    Aunque la anotación indica Profesor, el argumento también puede ser
    un objeto de cualquier clase hija, como ProfesorTitular.
    """

    print(
        f"\nTipo real del objeto: {type(profesor).__name__}"
    )

    # La versión ejecutada depende del tipo real del objeto.
    profesor.mostrar_informacion()


def main() -> None:
    """
    Función principal que demuestra el polimorfismo.
    """

    print("=" * 62)
    print("DEMOSTRACIÓN DE POLIMORFISMO")
    print("=" * 62)

    try:
        # Objeto de la clase padre.
        profesor_general = Profesor(
            nombre="Mateo Ramírez",
            departamento="Ciencias Básicas"
        )

        # Objetos de la clase hija.
        profesora_titular = ProfesorTitular(
            nombre="Valentina Herrera",
            departamento="Ingeniería",
            especialidad="Sistemas de control",
            anios_experiencia=12
        )

        segundo_titular = ProfesorTitular(
            nombre="Andrés Salazar",
            departamento="Ciencias Ambientales",
            especialidad="Gestión de recursos hídricos",
            anios_experiencia=9
        )

        # Una misma colección almacena objetos de la clase padre
        # y de la clase hija.
        profesores: list[Profesor] = [
            profesor_general,
            profesora_titular,
            segundo_titular
        ]

        # Se llama al mismo método para todos los objetos.
        for profesor in profesores:
            presentar_profesor(profesor)

    except (TypeError, ValueError) as error:
        print(f"\nNo fue posible crear el profesor: {error}")


if __name__ == "__main__":
    main()