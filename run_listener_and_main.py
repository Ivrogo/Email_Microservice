import multiprocessing

def run_main():
    import main as main
    template_request = {
        'name': 'Ivrogo',
        'message': 'esto es un test de rabbitMQ'
    }
    main.send_template_request(template_request)
    

def run_consumer():
    import consumer as consumer
    consumer.run_consumer()
    
    
if __name__ == '__main__':
    # Creamos 2 procesos para ambos main y consumer
    main_process = multiprocessing.Process(target=run_main)
    consumer_process = multiprocessing.Process(target=run_consumer)
    
    # Inicia ambos procesos
    main_process.start()
    consumer_process.start()
    
    
    # Espera que ambos procesos terminen
    main_process.join()
    consumer_process.join()