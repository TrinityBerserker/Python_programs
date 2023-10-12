import numpy as np
from sklearn.neural_network import MLPClassifier

# Datos de entrada
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
# Datos de salida esperados
y = np.array([0, 1, 1, 0])

# Crear el modelo de la red neuronal
model = MLPClassifier(hidden_layer_sizes=(4,), activation='relu', solver='adam', max_iter=20000)

# Entrenar el modelo
model.fit(X, y)

# Evaluar el modelo
accuracy = model.score(X, y)
print("Accuracy: %.2f%%" % (accuracy * 100))
