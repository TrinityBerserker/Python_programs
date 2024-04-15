import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Cargar los datos de vulnerabilidades en el sistema de seguridad
data = pd.read_csv("datos_vulnerabilidades.csv")

# Preprocesamiento de datos (eliminación de valores nulos, codificación de variables categóricas, etc.)

# Dividir los datos en conjuntos de entrenamiento y prueba
X = data.drop("vulnerable", axis=1)
y = data["vulnerable"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar un clasificador de bosque aleatorio
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Evaluar el modelo
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))
