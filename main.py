import requests
import json

def get_and_save_kpis_from_api():

    url = 'https://api.fusionplatform.io/insights/v2/1?scoredOnly=1'
    token = 'Bearer eyJraWQiOiJsVDFxNnVLNVJXYVBwejB0V2s4ekZXUnA4NGpTRmNPUEhtbTk0U1dFR2p3IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIwMHUycnp4M2E1MW52S3BKODQxNyIsIm5hbWUiOiJRdWVudGluIER1dmVyZ2UiLCJlbWFpbCI6InF1ZW50aW4uZHV2ZXJnZUBjaG9yZW9ncmFwaC5jb20iLCJ2ZXIiOjEsImlzcyI6Imh0dHBzOi8vd3BwLm9rdGEuY29tL29hdXRoMi9kZWZhdWx0IiwiYXVkIjoiMG9hOW8xaGtveVpYeHBraWI0MTciLCJpYXQiOjE3MjYwNTI3ODcsImV4cCI6MTcyNjA1NjM4NywianRpIjoiSUQuYTlsVmxTMnRJVmNoSEtNWUZHWUJ6NmhLOTJlNV81TjQ0Z0tkU1JTa3VvWSIsImFtciI6WyJtZmEiLCJvdHAiLCJwd2QiXSwiaWRwIjoiMDBvazZocHJNOGV1eUl3Mms0MTUiLCJub25jZSI6IkVNYVh6amU1UXJGUndHR3NFZlhRRXpPNUlvU2xuTFUwcFhQTDdmMW9KUktxZ1RqVHFSREJOdmNCQmF5N3FCM1oiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJxdWVudGluLmR1dmVyZ2VAY2hvcmVvZ3JhcGguY29tIiwiYXV0aF90aW1lIjoxNzI2MDUxMTA4LCJhdF9oYXNoIjoiUmg2cHVya0RnTEZ6ZXNsS3ZDTTFWZyIsImdyb3Vwc0Z1c2lvbiI6WyJHUlAtSFVCLUF1dGhOLWNob3Jlb2dyYXBoLUluc2lnaHRzUG9ydGZvbGlvR2VuZXJhbCIsIkdSUC1IVUItQXV0aE4tY2hvcmVvZ3JhcGgtUG9ydGZvbGlvX0FkbWluIiwiR1JQLUhVQi1BdXRoTi1jaG9yZW9ncmFwaC1JbnNpZ2h0c19BZG1pbiJdfQ.IyhElCjTeDTqx8NiSWWL8dkVHmrMJbDh8Esc4GppUenaAKVbWjsPMBUO3se2Fg-SJES616_7erUo7LZZIYpGwxY5qdL6VL6urtkVPybhZBN-AOKL0OfivfLoGa32ZXIObV_Zr3JzZttL5uvA-qGqJEMAHZUtc3og0a5ZKWGPLZrBpMqJofaOnGAQ-X6T_VgbSgP89Qh5W1fpzRFErZh5Pz6W1xs4CYnPRhXUgDZh5si7C6PAnVqkaa676OFizrAZNWPHuMpFb1S02aQ54aS8VEjI0DVr503tzahWZV-b8fEIpAJcmW41yr8lBN0wOXpKjh29f9yK1NuEAHeek4WpEA'
    
    data ={
        "filters": {
            "markets": [],
            "channels": [],
            "types": []
        },
        "user": {
            "email": "quentin.duverge@choreograph.com"
        }
    }
    resp = requests.post(url, headers={'Authorization': token, 'Content-Type': 'application/json'}, json= data)
    print(resp.json())
    # save the json
    with open('data.json', 'w') as f:
        json.dump(resp.json(), f, indent=4)



def extract_kpis_from_json():
    with open('data.json', 'r') as f:
        data = json.load(f)
    rows = data['rows']
    for row in rows[1:]:
        hierarchy = row['hierarchy']
        # remove the first element
        hierarchy.pop(0)
        print(hierarchy)


extract_kpis_from_json()
