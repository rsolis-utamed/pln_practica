# pln_practica
--- Proyecto para la asignatura PLN ( Máster Universitario en IA - UTAMED)---

Práctica de Procesamiento de Lenguaje Natural (PLN)

Este repositorio contiene la implementación de un agente inteligente utilizando LangChain 0.3 y los modelos de Google Gemini. El proyecto está diseñado para ejecutarse principalmente en Google Colab y demuestra el uso de Tool Calling y razonamiento avanzado.

🚀 Estructura del Repositorio

/code: Contiene los notebooks para extraer el corpus, modelar y crear un agente junto con un script para preprocesar los textos con la lógica del agente.
/models: Modelos preentrenados para el análisis de sentimiento y modelado de tópicos
/data: Recursos y archivos necesarios para el procesamiento.



🛠️ Requisitos e Instalación

Para evitar errores de compatibilidad con las versiones más recientes de la API de Google, asegúrate de instalar las dependencias exactas:

Python

!pip install -U -q langchain-google-genai langchain-community langchain
🔑 Configuración de la API Key

Este proyecto requiere una clave de API de Google AI Studio. Para configurarla de forma segura en Google Colab:

Ve al icono de la llave (🔑 Secretos) en la barra lateral.

Añade una nueva clave llamada GOOGLE_API_KEY.

Pega tu clave de API y activa el interruptor de "Acceso al notebook".

🤖 Modelos Compatibles (LangChain 0.3)
Si encuentras un error 404 NotFound al intentar usar gemini-pro, es debido a una discrepancia en la versión de la API (v1beta vs v1). En este código hemos actualizado la configuración para usar:

gemini-2.5-flash: Recomendado por su velocidad y eficiencia en agentes.
