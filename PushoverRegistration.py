from pushover_open_client import Client

inputConfigFile = "base.cfg"
outputConfigFile = "device.cfg"


with open(inputConfigFile, 'r') as inputConfig:
    jsonConfig = json.load(inputConfig)

self.domoticzAddress = jsonConfig["domoticzAddress"]
self.domoticzUser = jsonConfig["domoticzUser"]
self.domoticzPassword = jsonConfig["domoticzPassword"]


#Setup with a base config containing email and password
client = Client("base.cfg")

#Logs into Pushover's servers based on config
client.login()

#Registers a new device using the supplied device name
client.registerDevice("IFTTTDomoticz")

#Save the new device to a new config so registration
#can be bypassed in the future
client.writeConfig(outputConfigFile)

with open(outputConfigFile, 'r') as outputConfig:
    jsonConfig = json.load(outputConfig)

jsonConfig["domoticzAddress"] = domoticzAddress
jsonConfig["domoticzUser"] = domoticzUser
jsonConfig["domoticzPassword"] = domoticzPassword