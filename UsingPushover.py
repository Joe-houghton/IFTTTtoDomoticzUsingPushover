from pushover_open_client import Client
from CommandToDomoticz import Domoticz

domoticz = None
inputConfigFile = "device.cfg"


def messageCallback(messageList):
    # Process/do work with messageList!
    if(messageList):
        for message in messageList:
        
            #Do work with message here!
            print("Received: " + message.message + "\n")
            domoticz.ProcessMessage(message.message)

            #Make sure to acknowledge messages with priority >= 2
            if(message.priority >= 2):
                if(message.acked != 1):
                    client.acknowledgeEmergency(message.receipt)			
            
        #Make sure you delete messages that you recieve!
        client.deleteMessages(messageList[-1].id)

##Setups with a device configuration
client = Client(inputConfigFile)

# Process the domoticz part of the configuration
with open(inputConfigFile, 'r') as inputConfig:
    jsonConfig = json.load(inputConfig)

domoticzAddress = jsonConfig["domoticzAddress"]
domoticzUser = jsonConfig["domoticzUser"]
domoticzPassword = jsonConfig["domoticzPassword"]

# Create a new Domoticz instance
domoticz = new Domoticz(domoticzAddress, domoticzUser, domoticzPassword)

#Get any messages sent before the client has started
messageList = client.getOutstandingMessages()

#Do work with outstanding messages

#Make sure you delete messages that you recieve!
if(messageList):
    client.deleteMessages(messageList[-1].id)

#Pass our function as a parameter, this will run 'forever'
client.getWebSocketMessages(messageCallback)
