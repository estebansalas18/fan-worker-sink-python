# Fan-Worker-Sink (Python)

![Python](https://img.shields.io/badge/python-3.11-blue?logo=python)
![Status](https://img.shields.io/badge/status-ready-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

## 📌 Descripción

Este proyecto implementa un **sistema distribuido local** usando el patrón **Fan-Worker-Sink** en Python.

- **Fan**: genera y distribuye un lote de números aleatorios a los workers.  
- **Worker**: procesa los números en paralelo (eleva cada número al cuadrado).  
- **Sink**: recolecta todos los resultados y los devuelve **ordenados ascendentemente**.  

El objetivo del proyecto es **demostrar buenas prácticas de desarrollo, testing y arquitectura limpia**, listo para entornos profesionales y escalables.

## ⚒️ Estructura del Proyecto

```
fan-worker-sink-python/
├─ src/
│ ├─ init.py
│ ├─ fan.py             # Generación y distribución de números
│ ├─ worker.py          # Procesamiento en paralelo
│ ├─ sink.py            # Recolección y ordenamiento de resultados
│ └─ run.py             # Script principal para ejecutar el pipeline
│
├─ tests/
│ ├─ init.py
│ ├─ unit/              # Pruebas unitarias por módulo
│ └─ integration/       # Pruebas del flujo completo
│
├─ requirements.txt
├─ pytest.ini
├─ .gitignore
└─ README.md
```

## 🚀 Cómo ejecutar el proyecto

### 1️⃣ Instalar depedendencias

```
python -m venv .venv
source .venv/bin/activate       # Linux
.venv\Scripts\activate          # Windows

pip install -r requirements.txt
```

### 2️⃣ Ejecutar proyecto

```
python src/run.py
```

Esto generará un arreglo de 100 números aleatorios, los procesará en paralelo y devolverá los resultados **ordenados ascendentemente**.

## ✅ Tests y cobertura

### Ejecutar todas las pruebas

```
pytest
```

### Ejecutar solo pruebas unitarias o de integración

```
pytest tests/unit
pytest tests/integration
```

### Reporte de cobertura
- Coverage se genera automáticamente al correr `pytest`.
- Reporte HTML disponible en `html/index.html`
- Coverage mínima garantizada: 80% en módulos principales.

## 📋 Buenas prácticas implementadas
- Código modular con **arquitectura limpia**.
- Pruebas unitarias e integración completas.
- Cobertura mínima del 80%
- Compatible con **GitHub Actions** para CI/CD.
- Preparado para Docker y despliegue.

---

**📌 Juan Esteban Salas Flórez - Cloud Engineer**
