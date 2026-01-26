# CM_PLAN - Gestión de Configuración

Proyecto: MAX Inventory

## Elementos de Configuración (EC)

| EC | Ubicación | ¿Por qué es EC? | Quién lo modifica |
|---|---|---|---|
| README.md | / | Explica el proyecto y el uso del repositorio | Dev |
| CM_PLAN.md | / | Describe cómo se controlan cambios y versiones | Dev |
| CHANGELOG.md | / | Registra cambios por versión | Dev |
| SRS_v1.md | /docs/SRS/ | Define requisitos y alcance del sistema | Analista |
| Quality_Model.md | /docs/Quality/ | Define atributos y métricas de calidad | QA/Dev |
| Lifecycle_Impact.md | /docs/Lifecycle/ | Analiza el impacto del cambio por fase | Dev |
| config.example | /config/ | Guarda parámetros de ejecución del sistema | Dev |
| app.py | /src/ | Contiene la lógica principal del inventario | Dev |
| test_app.py | /tests/ | Valida que el stock se calcule bien | QA/Dev |

## Versionamiento mínimo
- Branch principal: main
- Commits claros

Ejemplos:
- docs: add SRS v1
- feat: add inventory logic
- test: add basic tests

## Control de cambios (flujo simple)
1) Se define el cambio como requisito (REQ-007)
2) Se trabaja el cambio y se deja evidencia (commit)
3) Se valida con prueba o ejecución
4) Se integra a main

## Línea base
Baseline: v1.0
# CM_PLAN - Gestión de Configuración

Proyecto: MAX Inventory

## Elementos de Configuración (EC)

| EC | Ubicación | ¿Por qué es EC? | Quién lo modifica |
|---|---|---|---|
| README.md | / | Explica el proyecto y el uso del repositorio | Dev |
| CM_PLAN.md | / | Describe cómo se controlan cambios y versiones | Dev |
| CHANGELOG.md | / | Registra cambios por versión | Dev |
| SRS_v1.md | /docs/SRS/ | Define requisitos y alcance del sistema | Analista |
| Quality_Model.md | /docs/Quality/ | Define atributos y métricas de calidad | QA/Dev |
| Lifecycle_Impact.md | /docs/Lifecycle/ | Analiza el impacto del cambio por fase | Dev |
| config.example | /config/ | Guarda parámetros de ejecución del sistema | Dev |
| app.py | /src/ | Contiene la lógica principal del inventario | Dev |
| test_app.py | /tests/ | Valida que el stock se calcule bien | QA/Dev |

## Versionamiento mínimo
- Branch principal: main
- Commits claros

Ejemplos:
- docs: add SRS v1
- feat: add inventory logic
- test: add basic tests

## Control de cambios (flujo simple)
1) Se define el cambio como requisito (REQ-007)
2) Se trabaja el cambio y se deja evidencia (commit)
3) Se valida con prueba o ejecución
4) Se integra a main

## Línea base
Baseline: v1.0
