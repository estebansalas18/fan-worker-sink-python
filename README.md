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
│ ├─ run_logs.py        # Script principal para ejecutar el pipeline (con Logs)
│ └─ run.py             # Script principal para ejecutar el pipeline
│
├─ tests/
│ ├─ init.py
│ ├─ unit/              # Pruebas unitarias por módulo
│ └─ integration/       # Pruebas del flujo completo
│
├─ .github/
│ └─ workflows/
│  └─ cicd.yaml         # Pipeline con pruebas automatizadas en GitHub Actions
│
├─ requirements.txt
├─ Dockerfile
├─ processing_log.csv   # Resultado de ejecución con logs
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

### 2️⃣ Ejecuciones disponibles

#### A. Modo estándar (sin logs)

Ejecuta el sistema con **100 números** y **3 workers** por defecto:
```
python -m src.run
```

Si deseas cambiar los valores, puedes pasarlos por consola:
```
python -m src.run 1000 4
```
→ Esto ejecutará el procesamiento con **1000 números** y **4 workers**.

#### B. Modo demostración (con logs + CSV)

Este modo sirve para mostrar visualmente cómo los workers están procesando en paralelo.
```
python -m src.run
```
Este modo:
- Usa **1000 números** y **3 workers** por defecto.
- Muestra en consola qué worker procesa cada número.
- Genera el archivo `processing_log.csv` en la carpeta raíz del proyecto.

El CSV incluye los datos de cada worker y el número procesado:

| worker_id | número_original   | número_procesado  |
|---------- |----------------   |-----------------  |
| worker_1  | 42                | 1764              |
| worker_2  | 17                | 289               |
| worker_3  | 95                | 9025              |

#### ✅ Resultado Final

Ambas formas devuelven al final la lista con los valores resultantes **ordenados ascendentemente**.

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
