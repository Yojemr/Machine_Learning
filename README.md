# Machine Learning

Laboratorio de Análisis y Desarrollo de Software. Incluye ejercicios de carga y exploración de datos con Pandas y NumPy, y un estimador académico del precio de vivienda con regresión lineal.

| Carpeta | Contenido |
| --- | --- |
| `data_load/` | Notebooks de Excel, CSV, API JSON y web scraping, con las ventas de ejemplo en `data/ventas_ejemplo.csv`. |
| `ml_models/linear_regression/backend/` | Modelo entrenado, script de entrenamiento y API con FastAPI. |
| `ml_models/linear_regression/frontend/` | Formulario en Django que consulta FastAPI y muestra el resultado en COP. |

## Preparar el entorno

Desde la raíz del repositorio, en PowerShell con Python 3.14:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r .\ml_models\linear_regression\backend\requirements.txt -r .\ml_models\linear_regression\frontend\requirements.txt -r .\data_load\requirements.txt
```

## Ejecutar el estimador

1. Inicia FastAPI con `.\ml_models\linear_regression\backend\iniciar_backend.ps1`.
2. En otra terminal, inicia Django con `.\ml_models\linear_regression\frontend\iniciar_frontend.ps1`.
3. Abre el [estimador](http://127.0.0.1:8001/) o prueba la API directamente en [Swagger](http://127.0.0.1:8000/docs).
4. Para cerrar FastAPI ejecuta `.\ml_models\linear_regression\backend\cerrar_backend.ps1`. Para cerrar Django usa `Ctrl+C` en su terminal.

| Operación | Función |
| --- | --- |
| `GET /modelo` | Consulta el rango de entrenamiento y los parámetros del modelo. |
| `POST /predecir` | Recibe una superficie en m² y devuelve el precio estimado en COP. |

Ejemplo de entrada para `POST /predecir`:

```json
{"superficie": 100}
```

El modelo se entrenó con ejemplos de **70 a 150 m²**, el rango que acepta el formulario de Django. Es una demostración académica basada únicamente en la superficie.

## Ejecutar las notebooks

Tras clonar, genera el Excel de práctica desde la raíz del repositorio:

```powershell
.\.venv\Scripts\python.exe -c "import pandas as pd; pd.read_csv('data_load/data/ventas_ejemplo.csv', parse_dates=['fecha']).to_excel('data_load/data/dataset_ventas.xlsx', sheet_name='dataset_ventas', index=False)"
```

Abre `data_load/` en VS Code con las extensiones Python y Jupyter. Elige como kernel el Python de `.venv` y ejecuta las celdas desde el inicio. Las notebooks de API y scraping necesitan conexión a Internet para consultar [JSONPlaceholder](https://jsonplaceholder.typicode.com/) y [Books to Scrape](https://books.toscrape.com/).
