# C1 · Simulación de cambio y su impacto por fase

Cambio simulado (REQ-007):
"Agregar exportación de movimientos a CSV."

| Fase | ¿Qué cambia? | EC afectados | Riesgo si no se controla | Evidencia de validación |
|---|---|---|---|---|
| Requisitos | Actualizar RF y criterio de aceptación | SRS_v1.md | Ambigüedad → retrabajo | Checklist + revisión |
| Diseño | Definir campos y formato del CSV | Lifecycle_Impact.md | Formato inconsistente | Diseño aprobado |
| Implementación | Crear función para exportar CSV | /src | Bugs / datos incompletos | Ejecución local |
| Pruebas | Agregar prueba de exportación | /tests | "funciona en mi PC" | Captura de ejecución |
| Release | Documentar el cambio en versión | CHANGELOG.md | Nadie sabe qué cambió | Changelog actualizado |
