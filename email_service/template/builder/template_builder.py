class TemplateBuilder:
    def build_template(self, template_data, company_logo_path):
        # Suponemos que tendremos un logo dentro del proyecto (pondre un placeholder)
        local_url = 'file://' + company_logo_path
        
        # Obtenemos los datos del template
        name = template_data.get('name', '')
        message = template_data.get('message', '')
        
        
        # Definimos una plantilla HTML basica
        email_template = f"""
        <html>
            <head></head>
            <body>
                <img src="{local_url}" alt="Logo de la empresa">
                <h1>Bienvenido, {name}!</h1>
                <p>{message}</p>
            </body>
        </html>
        """
            
        return email_template
    
    # Ejemplos de tipo de datos a añadir dentro de la funcion build_template:
    # template_data = {'name': 'demo', 'message': 'Hola, esto es una demo.'}
    # company_logo_path = 'ruta/al/logo.png' por ejemplo dentro de la misma carpeta de template seria 'Email_Microservice/email_service/template/logo.png'
    # email_template = TemplateBuilder().build_template(template_data, company_logo_path) 