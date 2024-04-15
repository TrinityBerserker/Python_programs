import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report

# Cargar los datos del conjunto de datos NSL-KDD
data = pd.read_csv("nsl-kdd.csv")

# Preprocesamiento de datos
# Eliminar columnas no relevantes y codificar variables categóricas

# Separar características y etiquetas
X = data.drop("label", axis=1)
y = data["label"]

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar los datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Entrenar un clasificador de redes neuronales
clf = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=1000, random_state=42)
clf.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = clf.predict(X_test)

# Imprimir métricas de evaluación del modelo
print(classification_report(y_test, y_pred))
