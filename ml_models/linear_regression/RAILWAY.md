# Regresión lineal en Railway

El servicio publica el formulario de Django y la API de FastAPI en un solo dominio. El punto de entrada `app.py` reúne las dos aplicaciones. El formulario calcula la estimación con el mismo modelo que usa la API.

## 1. Configurar el servicio

En el proyecto de Railway, abre el servicio conectado al repositorio [Machine_Learning](https://github.com/Yojemr/Machine_Learning) en la rama `main`. En **Settings**, usa Railpack y configura estos valores.

| Ajuste | Valor |
| --- | --- |
| **Root Directory** | `/ml_models/linear_regression` |
| **Start Command** | `python -m uvicorn app:app --host 0.0.0.0 --port "$PORT"` |

Railpack instala las dependencias de `requirements.txt` y usa Python 3.14 según el archivo `.python-version`. Si el servicio tiene una variable `RAILPACK_PYTHON_VERSION`, usa `3.14` como valor. Railway asigna `PORT`. La configuración se aplica desde el panel del servicio.

## 2. Variables y dominio

1. En **Variables**, conserva `DJANGO_SECRET_KEY` si ya existe. Para crear una clave nueva, genera el valor localmente con `python -c "from secrets import token_urlsafe; print(token_urlsafe(48))"` y guárdalo en Railway.
2. La variable `BACKEND_URL` se usa cuando Django se ejecuta por separado. Puedes retirarla del servicio unificado.
3. Pulsa **Deploy** y conserva el dominio público del servicio. Para generar uno, abre **Settings → Networking → Public Networking → Generate Domain**. Si Railway pide un puerto, usa el que figura en el registro de Uvicorn.

Si configuras una comprobación de salud en Railway, usa `/health`.

## 3. Verificar el despliegue

| Ruta | Resultado |
| --- | --- |
| `/` | Formulario de estimación en Django. |
| `/docs` | Swagger con `GET /modelo` y `POST /predecir`. |
| `/health` | Estado HTTP 200 tras cargar ambas aplicaciones. |

Ingresa **100 m²** en el formulario y compara el resultado con `POST /predecir` en Swagger usando `{"superficie": 100}`. Ambos deben mostrar **1.408.555.555,56 COP**.

[Root Directory en Railway](https://docs.railway.com/builds/build-configuration) · [Comandos de inicio](https://docs.railway.com/deployments/start-command) · [Python en Railpack](https://railpack.com/languages/python/)
