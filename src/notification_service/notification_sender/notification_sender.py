import pika
import json


def send_notification(notification_type, data):
    # Conecta al servidor RabbitMQ y envía la notificación
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    if notification_type == "email":
        # Declara la cola a la que se enviarán las notificaciones de correo
        channel.queue_declare(queue="email_queue")

        # Crea la notificación de correo electrónico
        email_notification = {
            "type": "email",
            "recipient": data.get("recipient"),
            "subject": data.get("subject"),
            "message": data.get("message"),
        }

        # Convierte la notificación a formato JSON y la envía
        channel.basic_publish(
            exchange="", routing_key="email_queue", body=json.dumps(email_notification)
        )
    elif notification_type == "template":
        # Declara la cola a la que se enviarán las solicitudes de plantilla
        channel.queue_declare(queue="template_queue")

        # Crea la solicitud de creación de plantilla
        template_request = {
            "type": "template",
            "data": {"name": data.get("name"), "message": data.get("message")},
        }

        # Convierte la solicitud a formato JSON y la envía
        channel.basic_publish(
            exchange="", routing_key="template_queue", body=json.dumps(template_request)
        )
    elif notification_type == "connection":
        # Declara la cola a la que se enviarán las solicitudes de conexión
        channel.queue_declare(queue="con_queue")

        # Crea la solicitud de conexión
        connection_request = {
            "type": "connection",
            "data": {
                "username": data.get("username"),
                "password": data.get("password"),
            },
        }

        # Convierte la solicitud a formato JSON y la envía
        channel.basic_publish(
            exchange="", routing_key="con_queue", body=json.dumps(connection_request)
        )

    print(f'Notificación de tipo "{notification_type}" enviada: {data}')

    connection.close()


if __name__ == "__main__":
    # Ejemplo de envío de notificación de correo
    email_data = {
        "recipient": "example@example.com",
        "subject": "Ejemplo de correo",
        "message": "Este es un mensaje de prueba.",
    }
    send_notification("email", email_data)

    # Ejemplo de solicitud de creación de plantilla
    template_data = {"name": "Nombre", "message": "Mensaje de prueba"}
    send_notification("template", template_data)

    # Ejemplo de solicitud de conexión
    connection_data = {"username": "usuario", "password": "contraseña"}
    send_notification("connection", connection_data)
