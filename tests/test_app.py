from src.app import InventoryService


def test_stock_ok() -> None:
    inv = InventoryService()
    inv.add_product("P001", "Teclado")
    inv.entry("P001", 5)
    inv.exit("P001", 2)
    assert inv.stock("P001") == 3
