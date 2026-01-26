from dataclasses import dataclass
from typing import Dict


@dataclass
class Product:
    code: str
    name: str
    stock: int = 0


class InventoryService:
    def __init__(self) -> None:
        self.products: Dict[str, Product] = {}

    def add_product(self, code: str, name: str) -> None:
        if code in self.products:
            raise ValueError("El producto ya existe")
        self.products[code] = Product(code=code, name=name)

    def entry(self, code: str, qty: int) -> None:
        if code not in self.products:
            raise ValueError("Producto no registrado")
        if qty <= 0:
            raise ValueError("Cantidad inválida")
        self.products[code].stock += qty

    def exit(self, code: str, qty: int) -> None:
        if code not in self.products:
            raise ValueError("Producto no registrado")
        if qty <= 0:
            raise ValueError("Cantidad inválida")
        if self.products[code].stock - qty < 0:
            raise ValueError("Stock insuficiente")
        self.products[code].stock -= qty

    def stock(self, code: str) -> int:
        if code not in self.products:
            raise ValueError("Producto no registrado")
        return self.products[code].stock


def main() -> None:
    inv = InventoryService()
    inv.add_product("P001", "Teclado")
    inv.entry("P001", 10)
    inv.exit("P001", 3)
    print("Stock actual:", inv.stock("P001"))


if __name__ == "__main__":
    main()
