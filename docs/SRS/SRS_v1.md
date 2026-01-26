# SRS v1 - MAX Inventory

## 1. Propósito
MAX Inventory es un mini-sistema para llevar control de inventario. Permite registrar productos, entradas y salidas, y consultar el stock actual.

## 2. Alcance
Incluye:
- Registro de productos
- Entradas y salidas
- Consulta de stock
- Listado de productos con stock

No incluye:
- Facturación
- Pagos
- Integración con sistemas externos

## 3. Actores
- Administrador
- Operador
- Auditor/Consulta

## 4. Requisitos funcionales (RF)
RF-001: Registrar producto (código, nombre).  
RF-002: Registrar entrada con cantidad.  
RF-003: Registrar salida con cantidad (sin stock negativo).  
RF-004: Consultar stock por código.  
RF-005: Listar productos con stock.

## 5. Requisitos no funcionales (RNF)
RNF-001: Responder en ≤ 2 segundos en el 95% de búsquedas.  
RNF-002: No guardar contraseñas reales en el repositorio.  
RNF-003: No permitir stock negativo.  
RNF-004: Debe existir al menos una prueba automatizada mínima.
