class TemplateBuilder:
    def build_template(self, data, company_logo_path):
        template = f"""
            <html>
                <head></head>
                <body>
                    <img src="file://{company_logo_path}" alt="Logo de la empresa">
                    <h1>Bienvenido, {data['name']}!</h1>
                    <p>{data['message']}</p>
                </body>
            </html>
        """
        return template
    
    # Ejemplos de tipo de datos a añadir dentro de la funcion build_template:
    # template_data = {'name': 'demo', 'message': 'Hola, esto es una demo.'}
    # company_logo_path = 'ruta/al/logo.png' por ejemplo dentro de la misma carpeta de template seria 'Email_Microservice/email_service/template/logo.png'
    # email_template = TemplateBuilder().build_template(template_data, company_logo_path) 