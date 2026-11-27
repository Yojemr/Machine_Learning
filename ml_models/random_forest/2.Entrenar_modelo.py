import os
import pandas as pd
from sklearn.model_selection import train_test_split # pip install scikit-learn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

def log(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

try:
    # =========================
    # 1. CARGA DEL DATASET AMPLIADO
    # =========================
    log("1. CARGA DEL DATASET AMPLIADO")
    script_dir = Path(__file__).resolve().parent
    dataset_path = script_dir / "data" / "dataset_medico_ampliado.csv"
    df = pd.read_csv(dataset_path)
    print(f"[OK] Dataset cargado: {df.shape[0]} filas, {df.shape[1]} columnas")
    
    # =========================
    # 2. SEPARAR FEATURES Y TARGET
    # =========================
    log("2. PREPARACIÓN DE DATOS")
    X = df.drop("diagnostico", axis=1)
    y = df["diagnostico"]
    
    print(f"[INFO] Features utilizadas ({len(X.columns)}):")
    for i, col in enumerate(X.columns, 1):
        print(f"   {i}. {col}")
    print(f"\n[INFO] Clases objetivo: {y.unique()}")
    
    # =========================
    # 3. DIVISIÓN TRAIN/TEST
    # =========================
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    print(f"\n[INFO] Split: Train {X_train.shape[0]} | Test {X_test.shape[0]}")
    
    # =========================
    # 4. ENTRENAMIENTO
    # =========================
    log("3. ENTRENAMIENTO DEL MODELO")
    model = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    print("[OK] Modelo entrenado")
    
    # =========================
    # 5. EVALUACIÓN
    # =========================
    log("4. EVALUACIÓN")
    y_pred = model.predict(X_test)
    accuracy = model.score(X_test, y_test)
    print(f"[INFO] Accuracy(Exactitud): {accuracy:.4f} ({accuracy*100:.2f}%)\n")
    print("[INFO] Classification Report:")
    print(classification_report(y_test, y_pred))
    print("[INFO] Matriz de confusión:")
    print(confusion_matrix(y_test, y_pred))
    
    # =========================
    # 6. IMPORTANCIA DE VARIABLES
    # =========================
    log("5. IMPORTANCIA DE VARIABLES")
    imp_df = pd.DataFrame({
        "Feature": X.columns,
        "Importancia (%)": (model.feature_importances_ * 100).round(2)
    }).sort_values("Importancia (%)", ascending=False)
    print(imp_df.head(15).to_string(index=False))
    
    # =========================
    # 7. GUARDAR MODELO
    # =========================
    log("6. GUARDANDO MODELO")
    subprocess.run("cls" if subprocess.os.name == "nt" else "clear", shell=True)
    script_dir = Path(__file__).resolve().parent
    models_dir = script_dir / "models"
    models_dir.mkdir(parents=True, exist_ok=True)
    modelo_path = models_dir / "modelo_random_forest_ampliado.pkl"
    joblib.dump(model, modelo_path)
    print(f"[OK] Modelo guardado en: {modelo_path}")
    
except FileNotFoundError:
    log("ERROR")
    print("[ERROR] No se encontró 'ml_models/random_forest/data/dataset_medico_ampliado.csv'")
    print("[INFO] Ejecuta primero '1.Crear_dataset.py'")
    exit(1)