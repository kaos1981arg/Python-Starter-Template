# Reglas del proyecto

## Stack tecnológico
- Python 3.14+ (gestionado por uv)
- Entorno y dependencias: uv
- Linting/Formato: Ruff
- Comprobación de tipos: Mypy (modo estricto)
- Pruebas: Pytest con cobertura seguir el flujo de trabajo de TDD escribir primero el test, verificar que falla y
           luego escribir el código para pasar el test
- Validación: Pydantic v2
- Registro: loguru

## Estándares de codificación
- SIEMPRE utilizar indicaciones de tipo en todas las firmas de funciones.
- Utilizar modelos Pydantic para las estructuras de datos en lugar de diccionarios sin formato.
- Preferir el diseño `src/` para todo el código fuente.
- Escribir cadenas de documentación en formato Google para la compatibilidad con MkDocs.

## Comandos de herramientas
- Instalar dependencias: `uv add <package>`
- Ejecutar la aplicación: `uv run python -m src.main`
- Ejecutar pruebas: `uv run pytest`
- Lint: `uv run ruff check --fix`

## Estilo
- No utilizar declaraciones `print()`; utilizar `loguru.logger`.
- Seguir el formato de estilo "Black" (gestionado por Ruff).
