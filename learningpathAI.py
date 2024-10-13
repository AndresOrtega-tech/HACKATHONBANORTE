import json
import numpy as np
import tensorflow as tf
import os

# Ruta donde se guardará el modelo
MODEL_PATH = 'learning_path_model.h5'

# Cargar los datos desde el archivo JSON
with open('adjustable_learning_path_data.json', 'r') as file:
    data = json.load(file)

# Crear un mapa de contenido dinámicamente
content_map = {}
for entry in data:
    for path in entry["learning_path"]:
        if path not in content_map:
            content_map[path] = len(content_map)  # Asigna un índice único para cada ruta de aprendizaje

# Preprocesar los datos
X = []
y = []

for entry in data:
    X.append(entry["answers"])
    
    # Convertir la ruta de aprendizaje a una lista de ceros y unos
    y_entry = np.zeros(len(content_map))  # Inicializar un vector de ceros
    for path in entry["learning_path"]:
        if path in content_map:
            y_entry[content_map[path]] = 1  # Asignar 1 si el tema está presente
    y.append(y_entry)

# Convertir listas a arreglos numpy
X = np.array(X)
y = np.array(y)

# Verificar si el modelo ya existe
if os.path.exists(MODEL_PATH):
    # Cargar el modelo existente
    model = tf.keras.models.load_model(MODEL_PATH)
    print("Modelo cargado desde el archivo.")
else:
    # Crear el modelo
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(X.shape[1],)),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(len(content_map), activation='sigmoid')  # Activación sigmoid para salida multi-label
    ])

    # Compilar el modelo
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Entrenar el modelo
    model.fit(X, y, epochs=1000, batch_size=10, validation_split=0.2)

    # Guardar el modelo entrenado
    model.save(MODEL_PATH)
    print("Modelo guardado en el archivo.")

# Evaluar el modelo
loss, accuracy = model.evaluate(X, y)
print(f"Loss: {loss}, Accuracy: {accuracy}")
