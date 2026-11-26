import joblib
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Predecir precios de viviendas segun la superficie en m2

# Datos de entrenamiento
x = np.array([[70], [80], [90], [100], [110], [120], [130], [140], [150]])
y = np.array([420000000, 800000000,900000000, 1500000000, 1800000000, 2100000000, 2400000000, 2700000000, 3000000000])

# Entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(x, y)

# # Predicciones de prueba
# y_pred = model.predict(x)

# # imprimir los coeficientes del modelo
# print("Coeficiente de regresión:", model.coef_)
# print("Término independiente:", model.intercept_)

# # Graficar datos reales
# plt.scatter(x, y, color='blue', label='Datos reales')

# # Graficar la línea de regresión
# plt.plot(x, y_pred, color='red', label='Línea de regresión')

# # Personalizar la gráfica
# plt.xlabel('Superficie (m2)')
# plt.ylabel('Precio (COP)')
# plt.title('Regresión Lineal: Precio de Viviendas según Superficie')
# plt.legend()
# plt.grid()

# # Mostrar la gráfica
# plt.show()

# Guardar(serializar) el modelo entrenado en un archivo
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model/linear_regression_model.joblib"

joblib.dump(model, MODEL_PATH)