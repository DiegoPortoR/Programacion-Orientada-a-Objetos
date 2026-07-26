"""
Ejercicio 4.7 - Clases abstractas

"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Clase abstracta principal de la jerarquía.

    Define los métodos que todas las clases concretas de animales
    deben implementar obligatoriamente.
    """

    @abstractmethod
    def obtener_nombre_cientifico(self) -> str:
        """
        Retorna el nombre científico del animal.
        """
        pass

    @abstractmethod
    def obtener_sonido(self) -> str:
        """
        Retorna el sonido característico del animal.
        """
        pass

    @abstractmethod
    def obtener_alimentacion(self) -> str:
        """
        Retorna el tipo de alimentación del animal.
        """
        pass

    @abstractmethod
    def obtener_habitat(self) -> str:
        """
        Retorna el hábitat principal del animal.
        """
        pass

    def mostrar_ficha(self) -> None:
        """
        Método concreto heredado por todos los animales.

        Utiliza los métodos abstractos implementados por cada
        clase concreta para mostrar su información.
        """

        print("=" * 58)
        print(f"ANIMAL: {self.__class__.__name__.upper()}")
        print("=" * 58)
        print(
            f"Nombre científico : "
            f"{self.obtener_nombre_cientifico()}"
        )
        print(f"Sonido            : {self.obtener_sonido()}")
        print(f"Alimentación      : {self.obtener_alimentacion()}")
        print(f"Hábitat           : {self.obtener_habitat()}")
        print("=" * 58)


class Canido(Animal, ABC):
    """
    Clase abstracta intermedia que representa a los cánidos.
    """

    def obtener_familia(self) -> str:
        """
        Retorna la familia taxonómica de los cánidos.
        """
        return "Canidae"


class Felino(Animal, ABC):
    """
    Clase abstracta intermedia que representa a los felinos.
    """

    def obtener_familia(self) -> str:
        """
        Retorna la familia taxonómica de los felinos.
        """
        return "Felidae"


class Perro(Canido):
    """
    Clase concreta que representa un perro doméstico.
    """

    def obtener_nombre_cientifico(self) -> str:
        return "Canis lupus familiaris"

    def obtener_sonido(self) -> str:
        return "Ladrido"

    def obtener_alimentacion(self) -> str:
        return "Carnívora"

    def obtener_habitat(self) -> str:
        return "Doméstico"


class Lobo(Canido):
    """
    Clase concreta que representa un lobo.
    """

    def obtener_nombre_cientifico(self) -> str:
        return "Canis lupus"

    def obtener_sonido(self) -> str:
        return "Aullido"

    def obtener_alimentacion(self) -> str:
        return "Carnívora"

    def obtener_habitat(self) -> str:
        return "Bosque"


class Gato(Felino):
    """
    Clase concreta que representa un gato doméstico.
    """

    def obtener_nombre_cientifico(self) -> str:
        return "Felis catus"

    def obtener_sonido(self) -> str:
        return "Maullido"

    def obtener_alimentacion(self) -> str:
        return "Carnívora"

    def obtener_habitat(self) -> str:
        return "Doméstico"


class Leon(Felino):
    """
    Clase concreta que representa un león.
    """

    def obtener_nombre_cientifico(self) -> str:
        return "Panthera leo"

    def obtener_sonido(self) -> str:
        return "Rugido"

    def obtener_alimentacion(self) -> str:
        return "Carnívora"

    def obtener_habitat(self) -> str:
        return "Sabana"


def mostrar_animales(animales: list[Animal]) -> None:
    """
    Recorre una colección de animales y muestra la ficha de cada uno.

    La función recibe referencias generales de tipo Animal,
    pero cada objeto ejecuta sus propios métodos.
    """

    for animal in animales:
        animal.mostrar_ficha()
        print()


def main() -> None:
    """
    Función principal del programa.

    Crea un arreglo de animales concretos y muestra los datos
    de cada uno mediante métodos polimórficos.
    """

    print("=" * 58)
    print("JERARQUÍA ABSTRACTA DE ANIMALES")
    print("=" * 58)
    print()

    animales: list[Animal] = [
        Perro(),
        Lobo(),
        Gato(),
        Leon()
    ]

    mostrar_animales(animales)


if __name__ == "__main__":
    main()