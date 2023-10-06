import unittest

from email_service.template.builder.template_builder import TemplateBuilder

class TestTemplateBuilder(unittest.TestCase):
    def test_build_template(self):
        # Datos de prueba
        template_data = {
            'from': 'noreply.icesoft@gmail.com',
            'name': 'er_jotx@hotmail.com',
            'message': 'Hola, esto es un mensaje de prueba'
        }
        company_logo_path = 'email_service/template/x17.jpg'
        
        # Construimos la plantilla con el TemplateBuilder
        template_builder = TemplateBuilder()
        actual_template = template_builder.build_template(template_data, company_logo_path)
        
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
        
        # Comprobamos si la plantilla generada coincide con la plantilla esperada
        self.assertEqual(actual_template.strip(), expected_template.strip())
        
        
if __name__ == '__main__':
    unittest.main()