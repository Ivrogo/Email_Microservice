import pika
import json
from src.database import database


def callback(ch, method, properties, body):
    try:
        # Decode el mensaje JSON recibido
        notification_data = json.loads(body)

        # Procesa la notificación
        notification_type = notification_data.get("type")
        if notification_type == "email":
            send_email_notification(notification_data)
        elif notification_type == "template":
            create_template(notification_data)
        elif notification_type == "connection":
            process_connection_request(notification_data)

        # Confirmar que el mensaje se ha entregado y eliminarlo de la cola
        ch.basic_ack(delivery_tag=method.delivery_tag)

    except Exception as e:
        # Maneja las excepciones apropiadamente (puede registrarlas o notificarlas)
        print(f"Error al procesar el mensaje: {e}")


def send_email_notification(notification_data):
    # Realiza el envío de correo aquí
    print(
        f'Enviando correo a {notification_data.get("recipient")} con asunto: {notification_data.get("subject")}'
    )

    # Guarda el tipo de notificación en la base de datos
    database.save_notification(notification_data.get("type"))


def create_template(notification_data):
    # Realiza la creación de plantilla aquí
    print(f'Creando plantilla con nombre: {notification_data.get("data").get("name")}')

    # Guarda el tipo de notificación en la base de datos
    database.save_notification(notification_data.get("type"))


def process_connection_request(notification_data):
    # Realiza el proceso de conexión aquí
    print(
        f'Procesando solicitud de conexión para usuario: {notification_data.get("username")}'
    )

    # Guarda la contraseña encriptada en la base de datos
    password = notification_data.get("password")
    encrypted_password = encrypt_password(password)
    database.save_encrypted_password(
        notification_data.get("password"), encrypted_password
    )

    # Guarda el tipo de notificación en la base de datos
    database.save_notification(notification_data.get("type"))


def encrypt_password(password):
    # Implementa la lógica de encriptación aquí
    # Devuelve la contraseña encriptada
    return password


def start_worker():
    # Configura la conexión a RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    # Declara la cola desde la cual se recibirán las notificaciones
    channel.queue_declare(queue="notification_queue")

    # Configura la función de devolución de llamada para procesar los mensajes
    channel.basic_consume(
        queue="notification_queue", on_message_callback=callback, auto_ack=False
    )

    print("Worker esperando notificaciones. Presiona CTRL+C para salir.")

    # Comienza a escuchar la cola indefinidamente
    channel.start_consuming()


if __name__ == "__main__":
    start_worker()
