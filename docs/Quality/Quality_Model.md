# Modelo de Calidad - ISO/IEC 25010 (adaptado)

Modelo elegido: ISO/IEC 25010  
Objetivo: convertir atributos de calidad en métricas verificables.

## 6 atributos + métricas

| Atributo | Definición | Métrica verificable | EC relacionados |
|---|---|---|---|
| Adecuación funcional | Cumple lo que se requiere | RF críticos cumplen | SRS, src, tests |
| Eficiencia de rendimiento | Respuesta rápida | ≤ 2s en 95% consultas (estrella) | src, tests |
| Confiabilidad | Evita fallas lógicas | 0 stock negativo | src, tests |
| Usabilidad | Fácil de usar | 90% tareas básicas en ≤ 3 min | README, SRS |
| Seguridad | Protege información | 0 secretos en texto plano (estrella) | config, src |
| Mantenibilidad | Fácil de modificar | cobertura mínima en funciones críticas | tests, src |

## Métricas estrella
1) Rendimiento: ≤ 2s en el 95% de búsquedas de stock.  
2) Seguridad: 0 contraseñas o llaves reales guardadas en el repositorio.
