import pika
import json

def send_template_request(template_request):
    template_request = {
        'name': 'Ivrogo',
        'message': 'esto es un test de rabbitMQ'
    }
    
    # Connexion a RabbitMQ
    conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = conn.channel()
    
    # Declaramos la cola
    queue_name = 'email_queue'
    channel.queue_declare(queue=queue_name)
    
    channel.basic_publish(exchange='', routing_key=queue_name, body=json.dumps(template_request))
    
    print(f'Se ha enviado la solicitud de plantilla: {template_request}')
    
    # Cerramos la connexion
    conn.close()

if __name__ == '__main__':
    template_request = {
        'name': 'Ivrogo',
        'message': 'esto es un test de rabbitMQ'
    }
    
    
    send_template_request(template_request)