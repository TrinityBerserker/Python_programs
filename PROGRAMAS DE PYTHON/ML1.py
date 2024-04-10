# Paso 1: Preparación de los Datos
import pandas as pd
from sklearn.model_selection import train_test_split

# Cargar datos
data = pd.read_csv("datos_transacciones.csv")

# Dividir datos en entrenamiento y prueba
X = data.drop("fraude", axis=1)  # Características
y = data["fraude"]  # Etiquetas
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Paso 2: Entrenamiento del Modelo
from sklearn.ensemble import RandomForestClassifier

# Crear y entrenar el modelo
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Paso 3: Evaluación del Modelo
from sklearn.metrics import classification_report, confusion_matrix

# Evaluar el modelo
y_pred = model.predict(X_test)
print("Matriz de Confusión:")
print(confusion_matrix(y_test, y_pred))
print("Reporte de Clasificación:")
print(classification_report(y_test, y_pred))

# Paso 4: Implementación del Modelo
# Ahora puedes usar "model" para predecir fraudes en nuevas transacciones
