from multiprocessing import connection
from kafka import KafkaConsumer
from json import loads
from json import dumps
from time import sleep
from debugpy import connect
import mysql.connector

consumer = KafkaConsumer(
    'topic1',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    # value_deserializer=lambda x: loads(x.decode('utf-8'))
)



mydb = mysql.connector.connect(host="localhost", database="Micra", user="root", passwd="secret")  #conexion con la base de datos

#Seleccionar e insertar las variables en la base de datos 

sql_get_user = """SELECT clientId FROM Clients WHERE clientId = %s"""
sql_insert_user = """INSERT INTO Clients (clientId,clientsName,clientsLastName,age,gender,weight,height,bloodPressureSist,bloodPressureDiast,cholesterol,smoker,drinking,disability,
previousPathology,postalCode) Values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
# transport = {'Bike':'1', 'Train':'2', 'Car':'3', 'Walking':'4'}



for event in consumer:                            
    event_data = event.value
    get_data_tuple = (event_data[0],)
    cursor = mydb.cursor(buffered=True)
    cursor.execute(sql_get_user, get_data_tuple)
    records = cursor.fetchall()             

    user = event_data[1]                            #Falla aqui por que en el producer tenemos que hacer con un buble for que nos mande lo mande de 1 en 1
    if cursor.rowcount == 0:
        cursor.close()
        insert_data_tuple = (user["id"], user["name"], user["last_name"], user["age"], user["gender"], user["weight"], user["height"], user["bloodpressure_sist"], 
                             user["bloodpressure_diast"], user["cholesterol"], True if user["smoker"] == '1' else False, user["drinking"], True if user["disability"] == '1' else False,
                             True if user["previouspatology"] == '1' else False, user["cp"])
        cursor = mydb.cursor(buffered=True)
        cursor.execute(sql_insert_user, insert_data_tuple)
        mydb.commit()

    cursor.close()

    


for event in consumer:
    event_data = event.value
    # Do whatever you want
    print(event_data)
    sleep(2)



#CONCLUSIÓN: El problema está en la manera que nos da los datos el producer.py