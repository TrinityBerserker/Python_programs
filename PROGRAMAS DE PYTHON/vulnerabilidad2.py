import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Cargar los datos de los registros de eventos de seguridad
data = pd.read_csv("datos_registros_eventos.csv")

# Seleccionar las características relevantes y normalizar los datos
X = data[['feature1', 'feature2', 'feature3']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test = train_test_split(X_scaled, test_size=0.2, random_state=42)

# Entrenar un modelo de detección de anomalías con Isolation Forest
clf = IsolationForest(contamination=0.05)
clf.fit(X_train)

# Predecir las anomalías en los datos de prueba
y_pred = clf.predict(X_test)

# Evaluar las predicciones
y_pred[y_pred == 1] = 0  # Anomalía si el valor es 1
y_pred[y_pred == -1] = 1  # No anomalía si el valor es -1

# Imprimir métricas de evaluación del modelo
print(classification_report(y_test, y_pred))
