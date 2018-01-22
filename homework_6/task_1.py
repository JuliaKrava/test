import requests

roles_data = {
        "id" : 5,
        "name": "Severus Snape",
        "type": "Wizard",
        "level": 50,
        "book": 1
}

roles_data2 = {
        "id" : 35,
        "name": "Severus Snape",
        "type": "best - Wizard - ever",
        "level": 150,
        "book": 1
}

r = requests.post("http://pulse-rest-testing.herokuapp.com/roles/", data=roles_data)
roles = r.json()
r1 = requests.put("http://pulse-rest-testing.herokuapp.com/roles/5/", data=roles_data2)
roles2 = r1.json()
r2 = requests.delete("http://pulse-rest-testing.herokuapp.com/roles/5/")
roles3 = r2.json()
print(roles, roles2, roles3)
