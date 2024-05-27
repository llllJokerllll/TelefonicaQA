# TelefonicaQA

## Prueba Técnica

Abre una terminal, navega al directorio raíz de tu proyecto y ejecuta el siguiente comando para instalar las dependencias listadas en requirements.txt:

pip install -r requirements.txt

## API Testing con Autenticación OAuth 2.0
Este proyecto contiene pruebas para verificar la respuesta del API de álbumes de JSONPlaceholder y maneja dos tipos de autenticación OAuth 2.0.

## Requisitos

Python 3.6 o superior
requests biblioteca de Python
unittest (incluido en la biblioteca estándar de Python)
Instalación
Clona el repositorio
Instala las dependencias:
pip install requests

## Ejecución Sin OAuth 2.0

python Ejercicio2_sinOAuth.py

## Ejecución Con Autenticación (Client Credentials)

Configura las variables `CLIENT_ID` y `CLIENT_SECRET` en `Ejercicio2_OauthCredentials.py`
Ejecuta las pruebas:

python Ejercicio2_OauthCredentials.py

## Ejecución Con Autenticación (Authorization Code)

Configura las variables `CLIENT_ID`, `CLIENT_SECRET`, `REDIRECT_URI` y `AUTH_CODE` en `Ejercicio2_OauthAuthorization.py`
Ejecuta las pruebas:

python Ejercicio2_OauthAuthorization.py

## BDD Given-When-Then

## Test de la API sin Autenticación

Given que la API de álbumes está disponible,
When realizamos una solicitud GET a la API de álbumes,
Then la respuesta debe tener un status code 200,
And el cuerpo de la respuesta debe contener una lista de álbumes con `userId`, `id` y `title`.

## Test de la API con Client Credentials

Given que la API de autenticación OAuth 2.0 está disponible,
When solicitamos un token de acceso usando `client_credentials`,
Then debemos recibir un token de acceso,
And cuando usamos ese token para hacer una solicitud GET a la API de álbumes,
Then la respuesta debe tener un status code 200,
And el cuerpo de la respuesta debe contener una lista de álbumes con `userId`, `id` y `title`.

## Test de la API con Authorization Code

Given que la API de autenticación OAuth 2.0 está disponible,
When solicitamos un token de acceso usando `authorization_code`,
Then debemos recibir un token de acceso,
And cuando usamos ese token para hacer una solicitud GET a la API de álbumes,
Then la respuesta debe tener un status code 200,
And el cuerpo de la respuesta debe contener una lista de álbumes con `userId`, `id` y `title`.
