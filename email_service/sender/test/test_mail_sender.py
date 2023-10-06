import unittest
from unittest.mock import Mock, patch
from email_service.sender.mail_sender import EmailSender
from email_service.template.builder.template_builder import TemplateBuilder


class TestSendEmail(unittest.TestCase):
    @patch('email_service.sender.mail_sender.smtplib.SMTP')
    def test_send_email(self, mock_smtp):
        # Configura el comportamiento del objeto Mock para simular el envío de correo
        mock_smtp_instance = mock_smtp.return_value
        mock_smtp_instance.sendmail.return_value = {}
        
        # Parámetros para enviar el correo
        company_logo_path = 'email_service/template/x17.jpg'
        template_data = {
            'from': 'noreply.icesoft@gmail.com',
            'name': 'er_jotx@hotmail.com',
            'message': 'Este es un mensaje de prueba'
        }
        
        # Utilizamos el Template Builder para construir el template del correo electronico esperado
        template_builder = TemplateBuilder()
        template = template_builder.build_template(template_data, company_logo_path)
        
        # Llama a la función para enviar el correo
        EmailSender.send_email(template_data)
        
        # Verifica si se llamaron a los métodos adecuados en el objeto SMTP
        expected_template = f"""
            <html>
                <head></head>
                <body>
                    <img src="file://{company_logo_path}" alt="Logo de la empresa">
                    <h1>Bienvenido, {template_data['name']}!</h1>
                    <p>{template_data['message']}</p>
                </body>
            </html>
        """
        mock_smtp.assert_called_once_with('smtp.gmail.com', 587)
        mock_smtp_instance.starttls.assert_called_once()
        mock_smtp_instance.login.assert_called_once()
        mock_smtp_instance.sendmail.assert_called_once_with(expected_template)
        mock_smtp_instance.quit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
