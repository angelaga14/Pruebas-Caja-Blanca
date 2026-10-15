# Actividad de pruebas de caja blanca

Archivos principales: `process.py`, `test_process.py` y `pytest.ini`.

## Instalación
```bash
python -m pip install pytest pytest-cov
```

## Ejecutar pruebas por marcador
```bash
python -m pytest -m statement -v
python -m pytest -m branch -v
python -m pytest -m path -v
```

## Cobertura por etapa
```bash
python -m pytest -m statement --cov=process --cov-report=term-missing
python -m pytest -m branch --cov=process --cov-branch --cov-report=term-missing
python -m pytest -m path --cov=process --cov-branch --cov-report=term-missing
```

**Atención:** aunque la consigna indica `--cov=process.py`, la sintaxis correcta en pytest-cov para medir este módulo es `--cov=process`. La primera puede arrojar "No data to report".

Los marcadores del archivo final permiten ejecutar las etapas por separado. Para mostrar 3 commits: comenzar el repositorio solo con los tests de sentencias, añadir los tests de ramas en el segundo commit, y los de caminos en el tercero. El repositorio remoto debe crearse desde tu cuenta.

## Ejemplo de commits (en tu equipo)
```bash
git init
git add process.py pytest.ini test_process.py
git commit -m "Etapa 1: cobertura de sentencias"
# Después de añadir los tests de ramas:
git add test_process.py
git commit -m "Etapa 2: cobertura de ramas"
# Después de añadir los tests de caminos:
git add test_process.py
git commit -m "Etapa 3: cobertura de caminos"
git remote add origin URL_DE_TU_REPOSITORIO
git branch -M main
git push -u origin main
```

**Nota:** Los PNG y el PDF son evidencia de ejecuciones reales en un entorno de ejemplo, no capturas de tu propia consola. Usa tu terminal para realizar tu entrega auténtica.
