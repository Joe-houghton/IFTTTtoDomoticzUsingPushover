from py_pushover_open_client.pushover_open_client import *
from CommandToDomoticz.CommandToDomoticz import *
import json

domoticz = None
client = None
inputConfigFile = "device.cfg"


def messageCallback(messageList):
    try:
        # Process/do work with messageList!
        if(messageList):
            for message in messageList:
        
                #Do work with message here!
                print("Received: " + message.message + "\n")
                #domoticz.PrintObject()
                domoticz.ProcessCommand(message.message)

                
                #Make sure to acknowledge messages with priority >= 2
                if(message.priority >= 2):
                    if(message.acked != 1):
                        client.acknowledgeEmergency(message.receipt)			
            
            #Make sure you delete messages that you recieve!
            client.deleteMessages(messageList[-1].id)
    except Exception as inst:
        print(type(inst))    # the exception instance
        print(inst.args)     # arguments stored in .args
        print(inst)          # __str__ allows args to be printed directly,
                             # but may be overridden in exception subclasses
        x, y = inst.args     # unpack args

def main():
    ##Setups with a device configuration
    global client
    client = Client(inputConfigFile)

    # Process the domoticz part of the configuration
    with open(inputConfigFile, 'r') as inputConfig:
        jsonConfig = json.load(inputConfig)

    domoticzAddress = jsonConfig["domoticzAddress"]
    domoticzUser = jsonConfig["domoticzUser"]
    domoticzPassword = jsonConfig["domoticzPassword"]

    # Create a new Domoticz instance
    global domoticz
    domoticz = Domoticz(domoticzAddress, domoticzUser, domoticzPassword)

    domoticz.PrintObject()

    #Get any messages sent before the client has started
    messageList = client.getOutstandingMessages()

    #Do work with outstanding messages

    #Make sure you delete messages that you recieve!
    if(messageList):
        client.deleteMessages(messageList[-1].id)

    print("Request for Messages sent")
    #Pass our function as a parameter, this will run 'forever'
    client.getWebSocketMessages(messageCallback)



if __name__ == '__main__':
    main()
