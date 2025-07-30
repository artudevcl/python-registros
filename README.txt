Como iniciar el proyecto

1. Clonar proyecto y luego ir a la raiz del proyecto.

2. Configurar un .env para el proyecto (Dejar en la raiz del proyecto).   

3. Tener docker arriba y Ejecutar docker-compose up -d --build
 con eso esperamos levantar PostgreSQL y el servicio Api.

4. Servicio/bd online en puertos y direcciones por defecto. http://localhost:8000
Documentación Interactiva (Swagger UI):  http://localhost:8000/docs
Endpoint en: http://localhost:8000/users/register

Datos prueba:

{
    "name": "Usuario Prueba",
    "email": "usuario.prueba@dominio.cl",
    "password": "PassWord123",
    "phones": [
        {
            "number": "987654321",
            "citycode": "1",
            "contrycode": "56"
        }
    ]
}
