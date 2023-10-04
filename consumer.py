import pika
import json

from email_service.template.builder.template_builder import TemplateBuilder

COMPANY_LOGO_PATH = 'email_service/template/x17.jpg'

def callback(ch, method, properties, body):
    # Cuando se recibe un mensaje de la cola
    template_data = json.loads(body)
    
    # Procesamos la solicitud
    template_builder = TemplateBuilder()
    email_template = template_builder.build_template(template_data, COMPANY_LOGO_PATH)
    
    print(f'Solicitud de plantilla procesada: {template_data}')
    print(f'Plantilla de correo generada: {email_template}')
    

def run_consumer():
    while True:
        # Connectamos a RabbitMQ
        conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = conn.channel()

        # Declaramos la cola
        queue_name = 'email_queue'
        channel.queue_declare(queue=queue_name)

        print('Esperando solicitudes de plantilla. Para salir, presiona CTRL+C')

        # Configuramos la función de devolución de llamada para procesar los mensajes
        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

        # Comienza a escuchar la cola
        channel.start_consuming()

if __name__ == '__main__':
    run_consumer()

    
    
    