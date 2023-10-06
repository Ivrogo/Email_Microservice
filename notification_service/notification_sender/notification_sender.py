import pika
import json


def send_notification(event_name, data):
    conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = conn.channel()
    
    # Declaramos una cola para enviar las notificaciones
    notification_queue = 'notification_queue'
    channel.queue_declare(queue=notification_queue)
    
    
    notification = {
        'event_name': event_name,
        'data': data
    }
    
    # Enviamos el mensaje a la cola de notificaciones de RabbitMQ
    channel.basic_publish(exchange='', routing_key=notification_queue, body=json.dumps(notification))
    
    print(f'Notificación enviada para el evento {event_name}')
    
    conn.close()
    

if __name__ == '__main__':
    event_name = 'send_email'
    template_data = {
        'from': 'noreply.icesoft@gmail.com',
        'name': 'er_jotx@hotmail.com',
        'message': 'esto es una demo'
    }
    
    send_notification(event_name, template_data)