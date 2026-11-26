# Regresión lineal en Railway

El estimador usa dos servicios en el mismo proyecto y entorno de Railway. FastAPI carga el modelo y publica Swagger. Django muestra el formulario y consulta la API desde el servidor.

## 1. Configurar los servicios

Conecta ambos servicios al repositorio [Machine_Learning](https://github.com/Yojemr/Machine_Learning) y selecciona la rama con el código a desplegar. Usa Railpack y configura cada servicio en **Settings**.

| Servicio | Root Directory | Start Command |
| --- | --- | --- |
| `Backend` | `/ml_models/linear_regression/backend` | `python -m uvicorn main:app --host 0.0.0.0 --port "$PORT"` |
| `Frontend` | `/ml_models/linear_regression/frontend` | `gunicorn --bind "0.0.0.0:$PORT" wsgi:application` |

En **Variables** de ambos servicios, define `RAILPACK_PYTHON_VERSION` con el valor `3.14`. Railway asigna `PORT` y Railpack instala el `requirements.txt` de cada carpeta. FastAPI carga `model/linear_regression_model.joblib` con la versión de scikit-learn declarada en sus requisitos.

Este procedimiento usa el panel de Railway. La opción **Config-as-code → Add File Path** corresponde a `railway.toml` y `railway.json`, cuyo soporte termina el **1 de diciembre de 2026**. [Aviso oficial de Railway](https://docs.railway.com/config-as-code)

## 2. Publicar y conectar

1. Despliega `Backend`. En **Settings → Networking → Public Networking**, selecciona **Generate Domain** y abre `/docs` en ese dominio.
2. En **Variables** de `Frontend`, define `DJANGO_SECRET_KEY` con una clave aleatoria propia. Puedes generarla localmente con `python -c "from secrets import token_urlsafe; print(token_urlsafe(48))"`. Guarda el valor solo en Railway.
3. En `Frontend`, define `BACKEND_URL` como `https://${{Backend.RAILWAY_PUBLIC_DOMAIN}}`. Si el servicio tiene otro nombre, usa ese nombre en la referencia.
4. Despliega `Frontend` y genera su dominio público. Si lo generas después del primer despliegue, vuelve a desplegar para que Django reciba `RAILWAY_PUBLIC_DOMAIN`.

Django usa `BACKEND_URL` para hacer predicciones y construir el enlace a Swagger. En Railway, también necesita `DJANGO_SECRET_KEY` y toma el dominio permitido de `RAILWAY_PUBLIC_DOMAIN`.

## 3. Comprobar el despliegue

- En el dominio del backend, abre `/docs`, ejecuta `GET /modelo` y luego `POST /predecir` con `{"superficie": 100}`. La respuesta debe incluir `precio_estimado_cop`.
- En el dominio del frontend, ingresa `100` en el formulario y verifica que muestre el mismo valor en pesos colombianos. **Ver documentación en Swagger** debe abrir el dominio del backend.
- Si Railpack no detecta Python, revisa que **Root Directory** apunte a la carpeta que contiene el `requirements.txt` del servicio. Si Django devuelve `400`, comprueba el dominio permitido. Si el formulario devuelve `403`, revisa que se abra por HTTPS y que Django conserve el ajuste del proxy y el token CSRF.

[Monorepos en Railway](https://docs.railway.com/deployments/monorepo) · [Python en Railpack](https://railpack.com/languages/python/) · [Proxy de Railway](https://docs.railway.com/networking/public-networking/specs-and-limits) · [Configuración de Django](https://docs.djangoproject.com/en/5.2/ref/settings/)
