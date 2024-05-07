import requests
import json

url = "http://localhost:5050/"

with open("storage.txt", "r") as f:
    
    name = f.readlines()

if name[0].endswith(" "):
    
    name[0] = name[0][:-1]

data = {
    "name": str(name[0])
}

json = json.dumps(data)

print(json)

response = requests.post(url, json=json)

if response.status_code == 200:
    
    with open("result.txt", "w") as f:
    
        f.write(f"Saldo desta pessoa: R${response.text}")
    
    print(f"Saldo desta pessoa: R${response.text}")

else:
    
    print(f"Erro. Status: {response.status_code}")