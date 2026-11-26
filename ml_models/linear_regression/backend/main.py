from pathlib import Path

import joblib
from fastapi import FastAPI
from pydantic import BaseModel, Field

# Cargar el modelo existente una sola vez al iniciar la API.
MODEL_PATH = Path(__file__).resolve().parent / 'model' / 'linear_regression_model.joblib'
model = joblib.load(MODEL_PATH)

app = FastAPI(
    title='Regresión lineal: precio de viviendas',
    description='Ejemplo académico de predicción según la superficie. Datos de entrenamiento: 70 a 150 m².',
    version='1.0.0',
)


class Vivienda(BaseModel):
    superficie: float = Field(
        gt=0, allow_inf_nan=False, examples=[100], description='Superficie de la vivienda en m².'
    )


@app.get('/modelo', summary='Consultar el modelo')
def obtener_modelo():
    # Mostrar los parámetros aprendidos, sin volver a entrenar.
    return {
        'tipo': 'Regresión lineal',
        'entrada': 'Superficie en m²',
        'salida': 'Precio estimado en COP',
        'rango_entrenamiento_m2': [70, 150],
        'coeficiente': float(model.coef_[0]),
        'intercepto': float(model.intercept_),
    }


@app.post('/predecir', summary='Predecir el precio de una vivienda')
def predecir(vivienda: Vivienda):
    # predict recibe una tabla: una fila con la superficie indicada.
    precio = model.predict([[vivienda.superficie]])[0]
    return {
        'superficie_m2': vivienda.superficie,
        'precio_estimado_cop': round(float(precio), 2),
    }
