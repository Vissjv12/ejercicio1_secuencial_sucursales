import time


def consultar_inventario(nombre, productos, tiempo_consulta):
    """Aqui es donde se simula la consulta de las sucursales"""
    print(f"Consultando en {nombre}")
    time.sleep(tiempo_consulta)
    print(f" Hay {productos} productos disponibles")
    return productos


def main():
    print("CONSULTANDO")
    inicio = time.perf_counter()
    total_productos = consultar_inventario("Sucursal Norte", 120, 1.0)
    total_productos += consultar_inventario("Sucursal Sur", 85, 1.5)
    total_productos += consultar_inventario("Sucursal Centro", 200, 0.8)
    total_productos += consultar_inventario("Sucursal Este", 65, 1.2)
    total_productos += consultar_inventario("Sucursal Oeste", 150, 1.0)

    tiempo_total = time.perf_counter() - inicio
    print("Sucursales 5")
    print(f"Total de productos disponibles: {total_productos}")
    print(f"Tiempo total: {tiempo_total:.2f} segundos")


if __name__ == "__main__":
    main()
