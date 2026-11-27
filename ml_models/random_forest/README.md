# Random Forest

Este ejercicio académico usa un bosque aleatorio para clasificar casos simulados. El dataset contiene **5.000 registros sintéticos**, **34 variables** y cinco clases: infarto, neumonía, gripe, ansiedad y gastroenteritis. Las predicciones ilustran el aprendizaje supervisado. El modelo carece de validación clínica y sus salidas se usan solo con fines educativos.

## Archivos

| Archivo | Función |
| --- | --- |
| [1.Crear_dataset.py](1.Crear_dataset.py) | Genera los registros sintéticos y guarda el CSV. |
| [2.Entrenar_modelo.py](2.Entrenar_modelo.py) | Entrena y evalúa el clasificador con una división estratificada de 70 % para entrenamiento y 30 % para prueba. |
| [3.Predecir_enfermedad.py](3.Predecir_enfermedad.py) | Abre una interfaz en Streamlit para probar el clasificador con datos simulados. |
| [Dataset](data/dataset_medico_ampliado.csv) | Registros sintéticos con la etiqueta objetivo `diagnostico`. |
| [Modelo entrenado](models/modelo_random_forest_ampliado.pkl) | Modelo serializado con Joblib. |

## Ejecutar en local

Desde la raíz del repositorio, usa PowerShell con Python 3.14. Si ya tienes `.venv`, omite el primer comando.

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r .\ml_models\random_forest\requirements.txt
Set-Location .\ml_models\random_forest
..\..\.venv\Scripts\python.exe -m streamlit run .\3.Predecir_enfermedad.py
```

## Regenerar el dataset y el modelo

Estos comandos regeneran el CSV y el modelo en sus rutas dentro de `random_forest`. Ejecútalos desde la raíz del repositorio.

```powershell
.\.venv\Scripts\python.exe .\ml_models\random_forest\1.Crear_dataset.py
.\.venv\Scripts\python.exe .\ml_models\random_forest\2.Entrenar_modelo.py
```
