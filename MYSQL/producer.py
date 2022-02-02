from json import dumps
from black import json
from kafka import KafkaProducer
from faker import Faker                                         #Libreria para crear random dataset, importar pandas y guardarlo en un dataframe para poder realizar operaciones
import keyboard                                                 #Se utiliza para obtener el control toral del teclado, Para asignar a una tecla una función para que sea interactivo
import time
import random
from datetime import datetime
import copy

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

faker = Faker('es_ES')
USERS_TOTAL=100
users={}
lat_min=39.4
lat_max=39.5
lon_min=-0.3
lon_max=-0.4
vehicles=["Bike","Train","Car", "Walking"]

def initiate_data():
    global users
    for i in range(0,USERS_TOTAL):
        user={}
        user["id"]=faker.ssn()
        user["name"]=faker.first_name()
        user["last_name"]=faker.last_name()
        # user["friends"]=[]
        user["position"]={"lat":random.uniform(39.4, 39.5),"lon":random.uniform(-0.3, -0.4)}
        user["transport"]=random.choice(vehicles)
        user["age"]=random.uniform(16, 85)
        user["gender"]=random.choice(["man","woman"])
        user["weight"]=random.uniform(60, 110)
        user["height"]=random.uniform(150, 210)
        user["bodyfat"]=random.uniform(3, 45)
        user["bloodpressure_sist"]=random.uniform(90, 180)
        user["bloodpressure_diast"]=random.uniform(70, 120)
        user["cholesterol"]=random.uniform(150, 300)
        user["smoker"]=random.choice(["0","1"])
        user["drinking"]=random.uniform(0,7)
        user["disability"]=random.choice(["0","1"])
        user["previouspatology"]=random.choice(["0","1"])
        user["cp"]=random.randint(46001, 46025)
        user["time"]=datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        users[user["id"]]=user
        
    #La siguiente funcion no corresponde a este caso  
    # num=0
    # for element in users.items():
    #     print(f"Generating friends of {num} of {len(users)}")
    #     for i in range(0,random.randint(1,10)):
    #         friend=random.choice(list(users.values()))
    #         if friend["id"]!=element[0]:
    #             users[element[0]]["friends"].append(friend["id"])
    #         else:
    #             print("No friend of yourself") 
    #     num=num+1

    print("DATA GENERATED")        


def generate_step():
    global users
    global old
    old = copy.deepcopy(users)
    if len(users)>0:
        print("STEP")
        for element in users.items():
            users[element[0]]["time"]=datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            lat=users[element[0]]["position"]["lat"]
            lon=users[element[0]]["position"]["lon"]
            users[element[0]]["position"]["lon"]=lon+random.uniform(0.001, 0.005)
            users[element[0]]["position"]["lat"]=lat+random.uniform(0.001, 0.005)
            if lat>lat_max or lat<lat_min:
                users[element[0]]["position"]["lat"]=random.uniform(39.4, 39.5)
                users[element[0]]["transport"]=random.choice(vehicles)
            if lon>lon_max or lon<lon_min:
                users[element[0]]["position"]["lon"]=random.uniform(-0.3, -0.4)
    else:
        initiate_data()




# NO TOCAR

oldval={}
while True:
    try:  
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Exited the data generator')
            break  
        else:
            generate_step()
            # Place your code here
            print(users)
            print(old)
            # End Place for code
            time.sleep(2)
    except Exception as err:
        print(f"Unexpected {err}, {type(err)}")
        break  