import unittest
import json
from unittest.mock import Mock, patch
from notification_service.notification_sender.notification_sender import send_notification

class TestSendNotification(unittest.TestCase):
    def setUp(self):
        self.mock_pika = patch('notification_service.notification_sender.notification_sender.pika').start()
        self.mock_pika.BlockingConnection.return_value = self.mock_connection = Mock()
        self.mock_connection.channel.return_value = self.mock_channel = Mock()

    def tearDown(self):
        patch.stopall()

    def test_send_notification(self):
        # Ejecutamos la función de notificación
        event_name = 'send_email'
        template_data = {'name': 'demo', 'message': 'esto es una unittest demo'}
        send_notification(event_name, template_data)
        
        # Verifica que se llame a las funciones adecuadas de pika
        self.mock_pika.BlockingConnection.assert_called_once_with(self.mock_pika.ConnectionParameters(host='localhost'))
        self.mock_connection.channel.assert_called_once()
        self.mock_channel.queue_declare.assert_called_once_with(queue='notification_queue')
        
        # Verifica si es el mensaje enviado correcto
        expected_notification= {
            'event_name': event_name,
            'data': template_data
        }
        expected_notification_json = json.dumps(expected_notification)
        self.mock_channel.basic_publish.assert_called_once_with(
            exchange='',
            routing_key='notification_queue',
            body=expected_notification_json
        )
        
if __name__ == '__main__':
    unittest.main()
