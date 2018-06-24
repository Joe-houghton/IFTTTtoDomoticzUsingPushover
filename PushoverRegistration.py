from pushover_open_client import Client

#Setup with a base config containing email and password
client = Client("base.cfg")

#Logs into Pushover's servers based on config
client.login()

#Registers a new device using the supplied device name
client.registerDevice("PushBulletDomoticzIFTTT")

#Save the new device to a new config so registration
#can be bypassed in the future
client.writeConfig("device.cfg")