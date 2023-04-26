import requests
import os
import json

print("Get Server JAR\n")

loader_version = ""
installer_version = ""

def getFabricShit(mcversion):

    global loader_version
    global installer_version

    #Because fabric devs are fucking idiots, i have to do this dumbassery to get the loader and the fabric versions.
    #This just writes a json file that i can use to look up the latest versions cause it doesn't work for some reason through the fabric website'
    floader = requests.get("https://meta.fabricmc.net/v2/versions/loader/" + mcversion)
    data = json.loads(floader.content.decode("ascii"))
    loader_version = data[0]["loader"]["version"]

    finstaller = requests.get("https://meta.fabricmc.net/v2/versions/installer/")
    data = json.loads(finstaller.content.decode("ascii"))
    installer_version = data[0]["version"]

def getURL(serversion, mcversion):
    global URL
    if (serversion == "purpur"):
        URL = "https://api.purpurmc.org/v2/purpur/" + mcversion + "/latest/download"
    elif (serversion == "paper"):
        paperVer = open("paperver.txt", "w")
        paperVer.write(mcversion)
        paperVer.close()
        os.system('./gamimenopaper.sh')
        quit("Paper JARs get fetched by gamimenopaper.sh")
    elif (serversion == "fabric"):
        #URL = "$api"/"$version"/"$latest_loader"/"$latest_installer"/server/jar
        # i hope this fucking works
        global loader_version
        global installer_version
        getFabricShit(mcversion)
        URL = f"https://meta.fabricmc.net/v2/versions/loader/{mcversion}/{loader_version}/{installer_version}/server/jar"
    else:
        print("Couldn't fetch the server JAR requested")

        print("Server JAR name requested: " + serversion)
        print("Minecraft Version Requested: " + mcversion)
        quit()

    global filename
    filename = serversion + "-" + mcversion + ".jar"

def downloadJAR():
    print(URL)
    serverJar = requests.get(URL)
    with open(filename, "wb") as f:
        f.write(serverJar.content)
        f.close()
    print("Downloaded " + jar + "-" + mc)



jar = input("Server JAR name: ")
mc = input("Minecraft Version: ")
getURL(jar, mc)
downloadJAR()
