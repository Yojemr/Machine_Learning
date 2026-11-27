# Regresión lineal

Estimador académico del precio de vivienda en pesos colombianos (COP). Usa la superficie en m² como única variable y se entrenó con ejemplos de **70 a 150 m²**, el rango que acepta el formulario.

| Componente | Función |
| --- | --- |
| [Backend](backend/) | FastAPI carga el modelo guardado y expone las operaciones en Swagger. |
| [Frontend](frontend/) | Django muestra el formulario y el precio estimado. |
| [Punto de entrada](app.py) | Ejecuta Django y FastAPI en el mismo puerto. |

## Ejecutar en local

Desde la raíz del repositorio, usa PowerShell con Python 3.14. Si ya tienes `.venv`, omite el primer comando.

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r .\ml_models\linear_regression\requirements.txt
.\.venv\Scripts\python.exe -m uvicorn app:app --app-dir .\ml_models\linear_regression --host 127.0.0.1 --port 8000
```

Abre el [formulario](http://127.0.0.1:8000/) o [Swagger](http://127.0.0.1:8000/docs). Detén el servidor con `Ctrl+C`.

## Usar la API

| Operación | Función |
| --- | --- |
| `GET /modelo` | Devuelve el rango de entrenamiento, el coeficiente y el intercepto. |
| `POST /predecir` | Recibe la superficie en m² y devuelve el precio estimado en COP. |

Ejemplo para `POST /predecir`.

```json
{"superficie": 100}
```

El proyecto incluye el [modelo entrenado](backend/model/linear_regression_model.joblib). El [script de entrenamiento](backend/train.py) contiene los datos de ejemplo y vuelve a generar ese archivo al ejecutarse con las [dependencias del backend](backend/requirements.txt).

## Desplegar

La [guía de Railway](RAILWAY.md) describe cómo publicar el formulario y Swagger como un solo servicio.
