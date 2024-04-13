from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Datos de ejemplo
# X representará las características (condiciones climáticas) y y será la etiqueta (deberías llevar un paraguas o no)
X = [[0, 1], [1, 0], [1, 1], [0, 0], [2, 2], [2, 0], [2, 1]]
y = [1, 1, 1, 0, 1, 0, 1]  # 1: llevar paraguas, 0: no llevar paraguas

# Dividir los datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el clasificador de árbol de decisión
clf = DecisionTreeClassifier()

# Entrenar el modelo
clf.fit(X_train, y_train)

# Hacer predicciones en el conjunto de prueba
y_pred = clf.predict(X_test)

# Evaluar la precisión del modelo
accuracy = metrics.accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {accuracy * 100:.2f}%")

# Ahora puedes utilizar el modelo para predecir si debes llevar un paraguas para nuevas condiciones climáticas
new_conditions = [[0, 1]]  # Ejemplo: no está lloviendo, pero hay viento
prediction = clf.predict(new_conditions)

if prediction[0] == 1:
    print("Deberías llevar un paraguas.")
else:
    print("No necesitas llevar un paraguas.")
