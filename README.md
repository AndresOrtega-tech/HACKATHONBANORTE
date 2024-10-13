# HACKATHONBANORTE

## Finanzas AI Chatbot
## Tabla de Contenidos

* **Introducción
* **Características
* **Tecnologías Utilizadas
* **Estructura del Proyecto
* **Instalación
* **Uso
* * **Entrenamiento del Modelo
* * **Interacción del Chatbot
* * **Interacción con la Base de Datos
* **Ejemplos de API
* **Contribuciones
* **Licencia
* **Contacto

## Introducción
El Finanzas AI Chatbot es una aplicación diseñada para ayudar a los usuarios a aprender sobre finanzas personales. Utiliza modelos de aprendizaje automático para personalizar la experiencia de aprendizaje de los usuarios y proporciona respuestas instantáneas a preguntas comunes sobre finanzas. Este chatbot también genera caminos de aprendizaje basados en respuestas de encuestas y ofrece recomendaciones de productos financieros.

## Características
* **Chatbot Interactivo: Responde a preguntas de los usuarios sobre finanzas personales en lenguaje natural.
* **Generación de Caminos de Aprendizaje: Personaliza el contenido educativo en función de las respuestas de los usuarios.
* **Recomendaciones de Productos Financieros: Ofrece sugerencias de productos adaptadas a las necesidades del usuario.
* **Noticias Personalizadas: Proporciona artículos de noticias relevantes en el ámbito financiero.
* **Base de Datos Dinámica: Almacena y gestiona información en tiempo real utilizando Firestore.

## Tecnologías Utilizadas
* **Python: Lenguaje de programación principal.
* **TensorFlow: Framework para el aprendizaje profundo.
* **Transformers: Para la implementación del modelo de conversación del chatbot (DialoGPT).
* **Firestore: Base de datos en tiempo real de Google para el almacenamiento de datos.
* **Pydantic: Para la validación y gestión de datos.

## Estructura del Proyecto
### La estructura del proyecto es la siguiente:
finanzas_ai_chatbot

│


├── database.py     


├── ai_logic.py           # Lógica de aprendizaje automático

├── chatbot.py            # Implementación del chatbot

├── info.py               # Definiciones de modelos y funciones de base de datos

├── learningpathia.py     # Entrenamiento del modelo de aprendizaje automático

├── adjustable_learning_path_data.json  # Datos de entrada para el modelo

├── requirements.txt      # Dependencias del proyecto

└── README.md             # Documentación del proyecto



## Instalación
* **Instala las dependencias:
* * **Asegúrate de tener pip instalado y ejecuta:
pip install -r requirements.txt

* **Configura Google Cloud:
* * **Crea un proyecto en Google Cloud.
* * **Habilita la API de Firestore.
* * **Descarga la clave de la cuenta de servicio y configura las credenciales de autenticación.



## Uso
### Entrenamiento del Modelo
* Ejecuta learningpathia.py para entrenar el modelo de aprendizaje automático. Este script cargará los datos, entrenará el modelo y lo guardará para su uso posterior.
* * **python learningpathia.py

### Interacción del Chatbot
* Ejecuta chatbot.py para iniciar el chatbot y permitir la interacción con los usuarios.
* * **python chatbot.py

### Interacción con la Base de Datos
* Puedes usar las funciones en database.py e info.py para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en la base de datos de Firestore.
