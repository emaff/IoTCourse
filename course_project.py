import sys
import hat
import mqtt_handler
from graceful_killer import GracefulKiller
from utils import getserial
import json
import time


def main():
    #PUT HERE YOUR CODE
    sense_hat = hat.hat()
    cpu_serial_id = getserial()

    BROKER_URL = "broker.hivemq.com"
    BROKER_PORT = 1883
    CLIENT_ID = cpu_serial_id

    mqtt_client = mqtt_handler.mqtt_handler(broker=BROKER_URL, port=BROKER_PORT, client_id=CLIENT_ID)
    mqtt_client.connect()
    time.sleep(1)

    topic_temperature = f"IoTCourseData/{cpu_serial_id}/Temperature"
    topic_movement = f"IoTCourseData/{cpu_serial_id}/Movement"

    is_connected = mqtt_client.check_connection()

    grace_killer = GracefulKiller()

    if is_connected:
        print("Client connected to Broker!!")
        while not grace_killer.is_killed():
            timestamp = int(time.time())
            env_data = sense_hat.get_env()
            env_data['timestamp'] = timestamp

            motion_data = sense_hat.get_movement()
            motion_data['timestamp'] = timestamp

            print(f"ENV_DATA: {env_data}")
            print(f"MOV_DATA: {motion_data}")

            mqtt_client.publish(topic=topic_temperature, msg=json.dumps(env_data))
            mqtt_client.publish(topic=topic_movement, msg=json.dumps(motion_data))

            time.sleep(1) #Data Frequency

        mqtt_client.disconnect()
        sys.exit(0)
    



if __name__ == "__main__":
    main()
