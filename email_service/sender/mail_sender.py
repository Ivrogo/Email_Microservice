# email_sender.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email_service.template.builder.template_builder import TemplateBuilder

class EmailSender:
    def send_email(template_data):
        # Configurar el servidor de correo SMTP
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'noreply.icesoft@gmail.com'
        smtp_password = 'yvtkghbvcwkusmyg'
        
        template_builder = TemplateBuilder()
        email_body = template_builder.build_template(template_data, 'email_service/template/x17.jpg')

        # Conectar al servidor SMTP y enviar el correo
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(email_body)
            server.quit()
            print('Correo electrónico enviado con éxito')
        except Exception as e:
            print('Error al enviar el correo electrónico:', str(e))
