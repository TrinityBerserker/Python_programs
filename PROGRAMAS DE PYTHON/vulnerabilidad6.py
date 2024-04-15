import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Conv1D, MaxPooling1D, Flatten, Dense

# Cargar los datos del conjunto de datos de correos electrónicos
data = pd.read_csv("phishing_emails.csv")

# Preprocesamiento de datos
X = data['email_text']
y = data['label']

# Codificar las etiquetas de clase
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Tokenizar el texto de los correos electrónicos y convertirlos en secuencias numéricas
tokenizer = Tokenizer()
tokenizer.fit_on_texts(X)
X_sequences = tokenizer.texts_to_sequences(X)

# Ajustar las secuencias a una longitud fija y crear un arreglo numpy
max_sequence_length = 1000  # longitud máxima de la secuencia
X_pad = pad_sequences(X_sequences, maxlen=max_sequence_length)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_pad, y, test_size=0.2, random_state=42)

# Construir el modelo de CNN
embedding_dim = 50  # dimensión del embedding
vocab_size = len(tokenizer.word_index) + 1  # tamaño del vocabulario

model = Sequential([
    Embedding(vocab_size, embedding_dim, input_length=max_sequence_length),
    Conv1D(128, 5, activation='relu'),
    MaxPooling1D(5),
    Conv1D(128, 5, activation='relu'),
    MaxPooling1D(5),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
model.fit(X_train, y_train, epochs=5, batch_size=32, validation_data=(X_test, y_test))

# Evaluar el modelo en el conjunto de prueba
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Pérdida en el conjunto de prueba: {loss}")
print(f"Precisión en el conjunto de prueba: {accuracy}")
