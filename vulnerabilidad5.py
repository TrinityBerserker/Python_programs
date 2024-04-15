import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Cargar los datos del conjunto de datos KDD Cup 1999
data = pd.read_csv("kddcup.csv")

# Preprocesamiento de datos
# Eliminar columnas no relevantes y codificar variables categóricas

# Separar características y etiquetas
X = data.drop("label", axis=1)
y = data["label"]

# Normalizar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Construir el modelo de Autoencoder
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(32, activation='relu'),
    Dense(64, activation='relu'),
    Dense(X_train.shape[1], activation='sigmoid')
])

model.compile(optimizer='adam', loss='mse')

# Entrenar el modelo de Autoencoder
model.fit(X_train, X_train, epochs=10, batch_size=32, validation_data=(X_test, X_test))

# Reconstruir los datos de entrada y calcular el error de reconstrucción
X_train_pred = model.predict(X_train)
train_mse = np.mean(np.power(X_train - X_train_pred, 2), axis=1)

# Establecer un umbral para la detección de anomalías
threshold = np.percentile(train_mse, 95)

# Predecir anomalías en los datos de prueba
X_test_pred = model.predict(X_test)
test_mse = np.mean(np.power(X_test - X_test_pred, 2), axis=1)
y_pred = (test_mse > threshold).astype(int)

# Imprimir métricas de evaluación del modelo
print(classification_report(y_test, y_pred))
