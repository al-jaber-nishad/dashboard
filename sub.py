# python3.6

import random
import json
from paho.mqtt import client as mqtt_client

from datetime import datetime



# SQL portion -------------------->

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="CSMS"
)

mycursor = mydb.cursor()

if mydb.is_connected():
  print('connected with the database')
else:
  print('Eror in connecting with database!')



# --------------------------------->



broker = '202.168.255.20'
port = 1883
topic = "gateway/node1"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'bnmqtt-user'
password = 'w7tfg6wtg'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received '{msg.payload.decode()}' from '{msg.topic}' topic")
        json_data = msg.payload.decode()
        py_data = json.loads(json_data)
        # py_data["N"]
        temp = py_data["T"]
        humi = py_data["H"]
        # print(py_data["timestamp"])
        dTime = datetime.fromtimestamp(py_data["timestamp"])


        sql = "INSERT INTO monitoring_node1 (temperature, humidity, time) VALUES (%s, %s, %s)"
        val = (temp, humi, dTime)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")



    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
