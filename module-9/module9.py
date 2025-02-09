import requests, json


response = requests.get('http://dnd5eapi.co/api/conditions/charmed')

print("API Status code: ", response.status_code) #return the API status code

data = response.json()
print("\nData without formatting: ", data) #print the data response without formatting


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print("\nData with formatting: ", text)

jprint(response.json()) #print the response with the same formatting as the tutorial