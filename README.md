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


##################################################################################################
##################################################################################################

## Escalabilidad del Finanzas AI Chatbot
El Finanzas AI Chatbot ha sido diseñado con varios principios y arquitecturas que garantizan su escalabilidad, lo que le permite crecer y adaptarse a un número creciente de usuarios y a una cantidad cada vez mayor de datos sin comprometer el rendimiento. A continuación, se detallan los aspectos clave que contribuyen a su escalabilidad:

1. Arquitectura Basada en Microservicios
* Separación de Responsabilidades: El chatbot está estructurado en diferentes módulos (por ejemplo, chatbot.py, ai_logic.py, info.py y database.py), lo que permite actualizar, modificar o escalar partes específicas del sistema de manera independiente.
* Despliegue Independiente: Cada microservicio puede ser escalado de manera independiente, lo que significa que si se requiere más capacidad para el chatbot, se pueden añadir más instancias sin afectar al modelo de aprendizaje o a la base de datos.
2. Uso de Tecnologías en la Nube
* Google Cloud Firestore: Esta base de datos NoSQL es altamente escalable y puede manejar grandes volúmenes de datos. Firestore automáticamente gestiona la escalabilidad y la disponibilidad, permitiendo a la aplicación manejar más usuarios sin requerir configuraciones complicadas.
* Infraestructura en la Nube: Al utilizar Google Cloud para el almacenamiento y procesamiento de datos, la infraestructura puede adaptarse fácilmente a las necesidades cambiantes, como el aumento de usuarios o la expansión de las capacidades de procesamiento.
3. Modelos de Aprendizaje Automático
* Modelo de Aprendizaje Profundo: El uso de TensorFlow permite que el modelo de aprendizaje automático sea altamente eficiente y escalable. Puede ser entrenado en diferentes conjuntos de datos sin perder eficacia y se pueden agregar más datos a medida que crece la base de usuarios.
* Entrenamiento y Ajuste Continuos: La capacidad de reentrenar el modelo con nuevos datos garantiza que el sistema se mantenga relevante y efectivo a medida que cambian las necesidades de los usuarios.
4. Interfaz de API
* Interacción Basada en API: La implementación de funciones y clases que interactúan a través de APIs permite que diferentes componentes del sistema se comuniquen entre sí de manera eficiente y escalable. Esto facilita la integración con otros servicios y sistemas, lo que es esencial para la expansión futura.
* Posibilidad de Integración: La estructura basada en API permite que el chatbot se integre con otras aplicaciones y plataformas, facilitando su extensión y la adición de nuevas funcionalidades.
5. Capacidad de Análisis y Ajuste
* Monitorización de Rendimiento: Con herramientas de monitorización y análisis, se pueden identificar cuellos de botella y áreas de mejora, lo que permite realizar ajustes en tiempo real y escalar recursos según sea necesario.
* Flexibilidad en la Gestión de Recursos: La arquitectura permite ajustar los recursos de procesamiento y almacenamiento en función de la demanda, garantizando un rendimiento óptimo incluso con cargas de trabajo fluctuantes.

# INSTALACION
* git clone <URL_DEL_REPOSITORIO>
* cd finanzas_ai_chatbot
* curl -sSL https://install.python-poetry.org | python3 -
* poetry install

# USO
* python learningpathia.py

# EJEMPLOS DE APIS
