# ADR-001: Selección del Stack Tecnológico

## Estado
Aceptado

## Contexto
El proyecto requiere desarrollo web con backend, frontend y módulo de Machine Learning.

## Decisión
Se selecciona:

- Backend: FastAPI (Python)
- Frontend: React
- Base de datos: PostgreSQL
- ML: scikit-learn

## Justificación

- Python facilita integración con ML
- FastAPI permite desarrollo rápido y documentación automática
- React es ampliamente usado en la industria
- PostgreSQL es robusto y escalable

## Consecuencias

- Requiere conocimiento básico en Docker
- Necesidad de separación clara de módulos
