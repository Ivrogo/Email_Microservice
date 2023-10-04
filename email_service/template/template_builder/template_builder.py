class TemplateBuilder:
    def build_template(self, template_data, company_logo_path):
        # Suponemos que tendremos un logo dentro del proyecto (pondre un placeholder)
        with open(company_logo_path, 'rb') as logo_file:
            logo_content = logo_file.read()
        
        # Convertimos los bytes del logo en una cadena base64
        import base64
        logo_base64 = base64.b64encode(logo_content).decode('utf-8')
        
        # Definimos una plantilla HTML basica
        email_template = f"""
        <html>
            <head></head>
            <body>
                <img src="data:image/png;base64,{logo_base64}" alt="Logo de la empresa">
                <h1>Bienvenido, {{ name }}!</h1>
                <p>{{ message }}</p>
            </body>
        </html>
        """
        
        # Reemplazamos las variables de la plantilla con datos proporcionados (tiene que ser un diccionario de Python (key:value))
        for key, value in template_data.items():
            placeholder = "{{" + key + "}}"
            email_template = email_template.replace(placeholder, str(value))
            
        return email_template
    
    # Ejemplos de tipo de datos a añadir dentro de la funcion build_template:
    # template_data = {'name': 'demo', 'message': 'Hola, esto es una demo.'}
    # company_logo_path = 'ruta/al/logo.png' por ejemplo dentro de la misma carpeta de template seria 'Email_Microservice/email_service/template/logo.png'
    # email_template = TemplateBuilder().build_template(template_data, company_logo_path) 