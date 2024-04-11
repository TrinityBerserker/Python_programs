from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Paso 1: Cargar el conjunto de datos
iris = load_iris()
X = iris.data
y = iris.target

# Paso 2: Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Paso 3: Crear y entrenar el modelo
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)

# Paso 4: Realizar predicciones
y_pred = clf.predict(X_test)

# Paso 5: Evaluar el rendimiento del modelo
precision = accuracy_score(y_test, y_pred)
print("Precisión del modelo:", precision)

# Paso 6: Utilizar el modelo para hacer predicciones nuevas
nuevas_caracteristicas = [[5.1, 3.5, 1.4, 0.2]]  # Nuevas características de una flor
prediccion = clf.predict(nuevas_caracteristicas)
print("Predicción:", iris.target_names[prediccion])
