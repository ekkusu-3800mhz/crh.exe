from dotenv import load_dotenv
import os
import json


load_dotenv()

DATA_FILE = os.environ.get('QUEUE_DATA')


def get_data():
    with open(DATA_FILE, 'rt') as queue_data_object:
        data = json.loads(queue_data_object.read())
        queue_data_object.close()
    return data


def set_data(data):
    origin = get_data()
    origin['cabinets'] = data
    json_str = json.dumps(origin)
    with open(DATA_FILE, 'wt') as queue_data_object:
        queue_data_object.write(json_str)
        queue_data_object.close()
