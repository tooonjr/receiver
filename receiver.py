#Importando a biblioteca "Pika", responsável por fazer a conexão com o Rabbit
import pika

#Conectando também com o Broker e também localhost pois as duas aplicações estão locais
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
canal = connection.channel()

# Criando a fila recebedora, que deverá ser a mesma setada no envio.
canal.queue_declare(queue='thompson-queue')


#Criando metodo que irá receber as mensagens enviadas pelo sender.
def callback(ch, method, properties, body):
    from datetime import datetime, timezone
    data_atual = datetime.now()
    print(data_atual,": ",body)

#Instanciando o consumo e definindo que o receiver irá apenas aguardar as mensagens e ser acionado.
canal.basic_consume(queue='thompson-queue',
                    auto_ack=True,
                    on_message_callback=callback)

print('Waiting \n. Exit: CTRL+C')

canal.start_consuming()
