import json
from requests_toolbelt import sessions

ENDPOINT_KEY = "cars"
OUTPUT_JSON = []

with sessions.BaseUrlSession(base_url="https://random-data-api.com/") as client:

    def write_to_db_json():
        response = client.get('api/vehicle/random_vehicle')
        json_data = response.json()
        id_exists = list(filter(lambda i: i.get('id') ==
                                json_data['id'], OUTPUT_JSON))
        if len(id_exists) > 0:
            return
        else:
            OUTPUT_JSON.append(json_data)

    for _ in range(5):
        write_to_db_json()


with open('db.json', 'r+') as file:
    existing_data = json.load(file)
    if existing_data.get(ENDPOINT_KEY):
        for entry in OUTPUT_JSON:
            existing_data[ENDPOINT_KEY].append(entry)
    else:
        existing_data[ENDPOINT_KEY] = OUTPUT_JSON
    file.seek(0)
    file.write(json.dumps(existing_data))
