import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn.metrics import classification_report

# Cargar los datos del conjunto de datos CICIDS 2017
data = pd.read_csv("cicids_2017.csv")

# Preprocesamiento de datos
# Eliminar columnas no relevantes y codificar variables categóricas

# Separar características y etiquetas
X = data.drop("label", axis=1)
y = data["label"]

# Normalizar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Entrenar un modelo de detección de anomalías con DBSCAN
clf = DBSCAN(eps=0.5, min_samples=10)
clf.fit(X_scaled)

# Asignar etiquetas de anomalía (-1) y no anomalía (1) a los datos
y_pred = clf.labels_
y_pred[y_pred == 0] = 1  # Clases identificadas como normales
y_pred[y_pred == -1] = 0  # Clases identificadas como anormales

# Imprimir métricas de evaluación del modelo
print(classification_report(y, y_pred))
