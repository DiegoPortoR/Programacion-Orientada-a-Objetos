"""
Ejercicio 2.10 - Sobrecarga de métodos

"""

class Producto:
    """
    Clase base que representa un producto disponible en el restaurante.
    """

    def __init__(self, nombre: str, precio: float):
        if not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")

        if precio <= 0:
            raise ValueError("El precio del producto debe ser mayor que cero.")

        self.nombre = nombre
        self.precio = precio

    def obtener_descripcion(self) -> str:
        """
        Retorna el nombre y el precio del producto.
        """
        return f"{self.nombre}: ${self.precio:,.2f}"


class PrimerPlato(Producto):
    """Representa el primer plato de un pedido."""
    pass


class SegundoPlato(Producto):
    """Representa el segundo plato de un pedido."""
    pass


class Bebida(Producto):
    """Representa la bebida de un pedido."""
    pass


class Postre(Producto):
    """Representa el postre de un pedido."""
    pass


class Pedido:
    """
    Clase encargada de administrar y calcular el valor de un pedido.

    La sobrecarga se simula mediante el método calcular_pedido(),
    el cual puede recibir dos, tres o cuatro productos.
    """

    def __init__(self, numero: int):
        self.numero = numero
        self.productos = []
        self.total = 0.0

    def calcular_pedido(self, *productos: Producto) -> float:
        """
        Simula la sobrecarga del método calcular_pedido.

        Combinaciones permitidas:

        1. Primer plato y bebida.
        2. Primer plato, segundo plato y bebida.
        3. Primer plato, segundo plato, bebida y postre.

        :param productos: productos que conforman el pedido.
        :return: valor total del pedido.
        """

        if len(productos) == 2:
            self._validar_pedido_dos_productos(productos)

        elif len(productos) == 3:
            self._validar_pedido_tres_productos(productos)

        elif len(productos) == 4:
            self._validar_pedido_cuatro_productos(productos)

        else:
            raise ValueError(
                "El pedido debe contener dos, tres o cuatro productos."
            )

        self.productos = list(productos)
        self.total = sum(producto.precio for producto in self.productos)

        return self.total

    @staticmethod
    def _validar_pedido_dos_productos(productos: tuple) -> None:
        """
        Valida un pedido compuesto por primer plato y bebida.
        """

        primer_plato, bebida = productos

        if not isinstance(primer_plato, PrimerPlato):
            raise TypeError("El primer producto debe ser un primer plato.")

        if not isinstance(bebida, Bebida):
            raise TypeError("El segundo producto debe ser una bebida.")

    @staticmethod
    def _validar_pedido_tres_productos(productos: tuple) -> None:
        """
        Valida un pedido compuesto por primer plato,
        segundo plato y bebida.
        """

        primer_plato, segundo_plato, bebida = productos

        if not isinstance(primer_plato, PrimerPlato):
            raise TypeError("El primer producto debe ser un primer plato.")

        if not isinstance(segundo_plato, SegundoPlato):
            raise TypeError("El segundo producto debe ser un segundo plato.")

        if not isinstance(bebida, Bebida):
            raise TypeError("El tercer producto debe ser una bebida.")

    @staticmethod
    def _validar_pedido_cuatro_productos(productos: tuple) -> None:
        """
        Valida un pedido compuesto por primer plato,
        segundo plato, bebida y postre.
        """

        primer_plato, segundo_plato, bebida, postre = productos

        if not isinstance(primer_plato, PrimerPlato):
            raise TypeError("El primer producto debe ser un primer plato.")

        if not isinstance(segundo_plato, SegundoPlato):
            raise TypeError("El segundo producto debe ser un segundo plato.")

        if not isinstance(bebida, Bebida):
            raise TypeError("El tercer producto debe ser una bebida.")

        if not isinstance(postre, Postre):
            raise TypeError("El cuarto producto debe ser un postre.")

    def mostrar_factura(self) -> None:
        """
        Muestra en consola los productos y el total del pedido.
        """

        print("\n" + "=" * 50)
        print(f"PEDIDO N.º {self.numero}")
        print("=" * 50)

        for posicion, producto in enumerate(self.productos, start=1):
            print(
                f"{posicion}. "
                f"{producto.nombre:<30} "
                f"${producto.precio:>10,.2f}"
            )

        print("-" * 50)
        print(f"{'TOTAL':<33} ${self.total:>12,.2f}")
        print("=" * 50)


def main() -> None:
    """
    Función principal del programa.

    Crea diferentes productos y utiliza el método calcular_pedido
    con tres cantidades distintas de parámetros.
    """

    # Primeros platos
    crema_champinones = PrimerPlato(
        "Crema de champiñones",
        9500
    )

    ensalada_cesar = PrimerPlato(
        "Ensalada César",
        12000
    )

    sopa_tomate = PrimerPlato(
        "Sopa de tomate",
        8500
    )

    # Segundos platos
    pollo_plancha = SegundoPlato(
        "Pollo a la plancha",
        23000
    )

    pescado_limon = SegundoPlato(
        "Pescado al limón",
        28000
    )

    # Bebidas
    limonada = Bebida(
        "Limonada natural",
        6000
    )

    jugo_mango = Bebida(
        "Jugo de mango",
        7000
    )

    agua = Bebida(
        "Agua mineral",
        4500
    )

    # Postres
    torta_chocolate = Postre(
        "Torta de chocolate",
        9000
    )

    print("=" * 50)
    print("SISTEMA DE PEDIDOS DEL RESTAURANTE")
    print("=" * 50)

    try:
        # Caso 1:
        # Primer plato y bebida.
        pedido_1 = Pedido(1)
        pedido_1.calcular_pedido(
            crema_champinones,
            limonada
        )
        pedido_1.mostrar_factura()

        # Caso 2:
        # Primer plato, segundo plato y bebida.
        pedido_2 = Pedido(2)
        pedido_2.calcular_pedido(
            ensalada_cesar,
            pollo_plancha,
            jugo_mango
        )
        pedido_2.mostrar_factura()

        # Caso 3:
        # Primer plato, segundo plato, bebida y postre.
        pedido_3 = Pedido(3)
        pedido_3.calcular_pedido(
            sopa_tomate,
            pescado_limon,
            agua,
            torta_chocolate
        )
        pedido_3.mostrar_factura()

    except (ValueError, TypeError) as error:
        print(f"\nNo fue posible procesar el pedido: {error}")


if __name__ == "__main__":
    main()