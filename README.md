
# Nombre del Proyecto

Breve descripción del proyecto.

## Instalación

1. Clona el repositorio:
    ```sh
    git clone <url-del-repositorio>
    ```

2. Navega al directorio del proyecto:
    ```sh
    cd nombre-del-proyecto
    ```

3. Crea y activa un entorno virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

4. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

5. Crea la base de datos:
    ```sh
    python manage.py migrate
    ```

6. Creacion de primer usuario administrador:
   ```sh
    http://localhost:8000/api/register/

    "username": "admin",
    "email": "admin@gmail.com",
    "first_name": "admin",
    "last_name": "admin",
    "password": "12345",
    "phone": "1234567",
    "gender": "M",
    "role": "admin"

    ```