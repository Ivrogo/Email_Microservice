import pika
import json

from email_service.template.builder.template_builder import TemplateBuilder
from email_service.sender.mail_sender import EmailSender

def callback(ch, method, properties, body):
    try:
        # Decode el mensaje JSON recibido
        template_data = json.loads(body)

        # Procesa la solicitud de plantilla de correo
        template_builder = TemplateBuilder()
        email_template = template_builder.build_template(template_data)

        # Envía el correo electrónico
        email_sender = EmailSender()
        email_sender.send_email(email_template)

        # Confirmar que el mensaje se ha entregado y eliminarlo de la cola
        ch.basic_ack(delivery_tag=method.delivery_tag)

    except Exception as e:
        # Maneja las excepciones apropiadamente (puede registrarlas o notificarlas)
        print(f"Error al procesar el mensaje: {e}")

def start_worker():
    # Configura la conexión a RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Declara la cola desde la cual se recibirán las solicitudes de plantillas de correo
    channel.queue_declare(queue='email_queue')

    # Configura la función de devolución de llamada para procesar los mensajes
    channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=False)

    print('Worker del Servicio de Email esperando solicitudes de plantillas. Presiona CTRL+C para salir.')

    # Comienza a escuchar la cola indefinidamente
    channel.start_consuming()

if __name__ == '__main__':
    start_worker()
