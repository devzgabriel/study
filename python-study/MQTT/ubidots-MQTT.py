'''
MQTT connection with Ubidots
You can:
Write 3 variables
Read a button

'''
# Gabriel Silva - devzgabriel

import paho.mqtt.client as mqttClient
import time
import json
import random

# global variables

connected = False  # Stores the connection status
BROKER_ENDPOINT = "industrial.api.ubidots.com"
PORT = 1883
MQTT_USERNAME = ""  # Put here your TOKEN
MQTT_PASSWORD = ""
TOPIC = "/v1.6/devices/"
DEVICE_LABEL = "teleco"
VARIABLE_BUTTON = "botao"
VARIABLE_LABEL = "dispositivo"


def on_connect(client, userdata, flags, rc):
  if rc == 0:
    print("[INFO] Connected to broker")
    global connected  # Use global variable
    connected = True  # Signal connection

  else:
    print("[INFO] Error, connection failed")


def on_publish(client, userdata, result):
  print("[INFO] Published!")


def connect(mqtt_client, mqtt_username, mqtt_password, broker_endpoint, port):
  global connected

  if not connected:
    mqtt_client.username_pw_set(mqtt_username, password=mqtt_password)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_publish = on_publish
    mqtt_client.connect(broker_endpoint, port=port)
    mqtt_client.loop_start()

    attempts = 0

    while not connected and attempts < 5:  # Waits for connection
      print("[INFO] Attempting to connect...")
      time.sleep(1)
      attempts += 1

  if not connected:
    print("[ERROR] Could not connect to broker")
    return False

  return True


def publish(mqtt_client, topic, payload):
  try:
    mqtt_client.publish(topic, payload)
  except Exception as e:
    print("[ERROR] There was an error, details: \n{}".format(e))


def on_message(mqtt_client, obj, msg):
  # print("[INFO] value received: {}".format(float(msg.payload)))
  if float(msg.payload) == 0: 
    print("Botão não está pressionado")
  elif float(msg.payload) == 1: 
    print("Botão pressionado")


def on_subscribe(mqtt_client, obj, mid, granted_qos):
  print("[INFO] Subscribed!")


def listen_terminal():
  option = 0
  print(f"\n\n{'*'*10}    MENU    {'*'*10}")
  for disp in range(1,4):
    print(f'{disp}- Enviar informação dispositivo 0{disp}')
  print('4- Ler informação do botão')
  option = int(input('Escolha sua opção: '))
  print('Opção Salva') if 0<option<5 else print('Opção Inválida')
  return option


def send_data(option):
  print(f'Alterando dispositivo {option}!')

  # Simulates sensor values
  sensor_value = random.random() * 100

  # Builds Payload and topíc
  payload = json.dumps({VARIABLE_LABEL+f"_{option}": sensor_value})
  topic = "{}{}".format(TOPIC, DEVICE_LABEL)

  # Publishes values
  print("[INFO] Attempting to publish payload:")
  print(payload)
  publish(mqtt_client, topic, payload)


def recive_print_data():
  print('\n\nRecebendo informação...')

  mqtt_client.on_subscribe = on_subscribe

  topic_1 = "{}{}/{}/lv".format(TOPIC, DEVICE_LABEL, VARIABLE_BUTTON)
  print(topic_1)
  mqtt_client.subscribe(topic_1, 0)
  
  mqtt_client.on_message = on_message

  mqtt_client.unsubscribe(topic_1, 0)


def main(mqtt_client):

  if not connected:  # Connects to the broker
    connect(mqtt_client, MQTT_USERNAME, MQTT_PASSWORD, BROKER_ENDPOINT, PORT)

  option = listen_terminal()
  if 0<option<4: send_data(option)
  elif option==4: recive_print_data()
  else: print('Nenhuma ação será realizada')


if __name__ == '__main__':
  mqtt_client = mqttClient.Client()
  while True:
    main(mqtt_client)
    time.sleep(1)
