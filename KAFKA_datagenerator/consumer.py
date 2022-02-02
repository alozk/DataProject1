from multiprocessing import connection
from kafka import KafkaConsumer
from json import loads
from json import dumps
from time import sleep
import mysql.connector as sql_db 
import haversine as hs

users_dict = {}
#Connection to the Kafka server
consumer = KafkaConsumer(
    'topic_test',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group-id',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

#Connection to the MySQL server
mydb = sql_db.connect(host="localhost", user="root", passwd="root") 
cursor = mydb.cursor(buffered=True)
cursor.execute("use micra")

#SQL Request Preparation
get_user = """SELECT clientId FROM Clients WHERE clientId = %s"""
insert_user = """INSERT INTO Clients (clientId,clientsName,clientsLastName,age,gender,weight,height,bloodPressureSist,bloodPressureDiast,cholesterol,smoker,drinking,disability,
previousPathology,postalCode) Values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
insert_coordinates = """INSERT INTO ClientsCoordinates (clientsId,transportId,latitude, longitude, createDate) Values (%s,%s,%s,%s,%s)"""
call_insert_km = """call KMin(%s,%s,%s,%s);"""

#Distance Calculation Fonction
def calculate_distance(lat_origin, long_origin, lat_dest, long_dest):
    loc1=(lat_origin,long_origin)
    loc2=(lat_dest,long_dest)
    dis = hs.haversine(loc1,loc2)
    print(dis, lat_origin, long_origin, lat_dest, long_dest)
    return dis

transport = {'Bike': '1', 'Train': '2', 'Car': '3', 'Walking': '4'}
#Ready from the Producers Data
for event in consumer:                            
    event_data = event.value
    get_data_tuple = (event_data[0],)
    cursor = mydb.cursor(buffered=True)
    user = event_data[1]
    cursor.execute(get_user, get_data_tuple)
    records = cursor.fetchall()
#Injecting Clients Data
    if cursor.rowcount == 0:
        cursor.close()
        insert_data_tuple = (user["id"], user["name"], user["last_name"], user["age"], user["gender"], user["weight"], user["height"], user["bloodpressure_sist"], user["bloodpressure_diast"], user["cholesterol"], True if user["smoker"] == '1' else False, user["drinking"], True if user["disability"] == '1' else False, True if user["previouspatology"] == '1' else False, user["cp"])
        cursor = mydb.cursor(buffered=True)
        cursor.execute(insert_user, insert_data_tuple)
        mydb.commit()
#Injecting Coordinates Data
    cursor.close()
    insert_data_tuple_coordinates = (user["id"], transport[user["transport"]], user["position"]["lat"], user["position"]["lon"], user["time"])
    cursor = mydb.cursor(buffered=True)
    cursor.execute(insert_coordinates, insert_data_tuple_coordinates)
    mydb.commit()

    walking_distance = 0
    biking_distance = 0
#Injecting and Calculating kmcount Data   
    if user["id"] in users_dict:
        if users_dict[user["id"]]['Transport'] == "Walking":
            walking_distance = calculate_distance(users_dict[user["id"]]["Lat"], users_dict[user["id"]]["Lon"], user["position"]["lat"], user["position"]["lon"])
        if users_dict[user["id"]]['Transport'] == "Bike":
            biking_distance = calculate_distance(users_dict[user["id"]]["Lat"], users_dict[user["id"]]["Lon"], user["position"]["lat"], user["position"]["lon"])

    args = (user["id"], round(walking_distance,3),round(biking_distance,3),user["time"])
    cursor.close()
    cursor = mydb.cursor(buffered=True)
    cursor.execute(call_insert_km, args)
    mydb.commit()
    users_dict[user["id"]] = {'Transport': user["transport"], 'Time': user["time"], 'Lat': user["position"]["lat"], 'Lon': user["position"]["lon"]}



#sql_create_table_client = "CREATE TABLE Clients(clientId VARCHAR(255),clientsName VARCHAR(255),clientsLastName VARCHAR(255),age FlOAT,gender VARCHAR(255) ,weight FLOAT,height FLOAT,bloodPressureSist FLOAT,bloodPressureDiast FLOAT,cholesterol FLOAT,smoker VARCHAR(255),drinking FLOAT,disability VARCHAR(255),previousPathology VARCHAR(255),postalCode VARCHAR(255))"
#sql_create_table_Cor = "CREATE TABLE ClientsCoordinates (clientsId VARCHAR(255),transportId VARCHAR(255),latitude FlOAT, longitude FlOAT, createDate DATETIME)"
#sql_create_table_kmcount CREATE TABLE `kmcount` (`clientsId` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,`walking_distance` float DEFAULT NULL,`biking_distance` float DEFAULT NULL,`timecal` datetime)