import requests as r
import json


api = "https://meta.fabricmc.net/v2/versions/loader/1.19.4"

response = r.get(api)

data = json.loads(response.content.decode("ascii"))

print(data[0])

loader_version = data[0]["loader"]["version"]
installer_version = data[0]["version"]

print(loader_version, installer_version)
