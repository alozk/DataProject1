# NO TOCAR
from faker import Faker
import keyboard
import time
import random
from datetime import datetime
import haversine as hs

faker = Faker('es_ES')
USERS_TOTAL=100
users={}
lat_min=39.4
lat_max=39.5
lon_min=-0.3
lon_max=-0.4
vehicles=["Bike","Train","Car", "Walking"]
temp = 0

def initiate_data():
    global users
    for i in range(0,USERS_TOTAL):
        user={}
        user["id"]=faker.ssn()
        user["name"]=faker.first_name()
        user["last_name"]=faker.last_name()
        user["friends"]=[]
        user["position"]={"lat":random.uniform(39.4, 39.5),"lon":random.uniform(-0.3, -0.4)}
        user["transport"]=random.choice(vehicles)
        user["age"]=random.uniform(16, 85)
        user["gender"]=random.choice(["man","woman"])
        user["weight"]=random.uniform(60, 110)
        user["height"]=random.uniform(150, 210)
        user["bodyfat"]=random.uniform(3, 45)
        user["bloodpressure_sist"]=random.uniform(120, 180)
        user["bloodpressure_diast"]=random.uniform(70, 120)
        user["cholesterol"]=random.uniform(150, 300)
        user["smoker"]=random.choice(["0","1"])
        user["drinking"]=random.uniform(0,7)
        user["disability"]=random.choice(["0","1"])
        user["previouspatology"]=random.choice(["0","1"])
        user["time"]=datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        users[user["id"]]=user   
        print(user)
    num=0
    for element in users.items():
        print(f"Generating friends of {num} of {len(users)}")
        for i in range(0,random.randint(1,10)):
            friend=random.choice(list(users.values()))
            if friend["id"]!=element[0]:
                users[element[0]]["friends"].append(friend["id"])
            else:
                print("No friend of yourself") 
        num=num+1

    print("DATA GENERATED")        


def generate_step():
    global users
    global usersdup
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
    return users

def compare(users_generated , usersdup):
    i = 0
    kmcount = [0 for x in range(100)]
    for key, value in users_generated.items():
          #print(users[key])
          print(key)
          loc1=(usersdup[key].get('position').get('lat'),usersdup[key].get('position').get('lon'))
          print(loc1)
          loc2=(users_generated[key].get('position').get('lat'),users_generated[key].get('position').get('lon'))
          print(loc2)
          print(hs.haversine(loc1,loc2))
          kmcount[i] = hs.haversine(loc1,loc2)
          i = i + 1
    usersdup = users_generated.copy()
    return kmcount


# NO TOCAR

while True:

    try:  
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Exited the data generator')
            break  
        else:
            users_generated=generate_step()

            if(temp == 0):
                usersdup=users_generated.copy()
                temp = temp + 1
                print("temp is now 1")
            # Place your code here
            print("code")
            # End Place for code
            print(compare(users_generated, usersdup))

            time.sleep(2)

    except Exception as err:
        print(f"Unexpected {err}, {type(err)}")

#users.dict.get(key[005-30-4977]       
#print(users['005-30-4977'].get('position'))
#loc1=(users['005-30-4977'].get('position').get('lat'),users['005-30-4977'].get('position').get('lon'))
#loc2=(users['016-23-4344'].get('position').get('lat'),users['016-23-4344'].get('position').get('lon'))
#hs.haversine(loc1,loc2)

#usersdup = users


compare(users, usersdup)
#print(compare(users, usersdup))
