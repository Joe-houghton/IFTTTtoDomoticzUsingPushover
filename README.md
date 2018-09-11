# IFTTTtoDomoticzUsingPushover
Control Domoticz through using IFTTT via Pushover messaging service

First, lets get a Pushover account from https://pushover.net/ 

Make sure that python 3 is installed by running:
```
sudo apt-get install python3
```

Next, install all dependencies:
```
sudo pip3 install CommandToDomoticz py-pushover-open-client requests
```

Now lets copy this project, ready for configuring:
```
cd ~/
mkdir scripts
cd scripts
git clone https://github.com/Joe-houghton/IFTTTtoDomoticzUsingPushover.git
cd IFTTTtoDomoticzUsingPushover
```
## Configuration
Now edit the base configuration file
```
nano base.cfg
```
Fill out the "domoticzAddress" plus the user and password if your Domoticz requires one.
Next fill out your pushover email and password.
Save the base.cfg file.

Now we need to run the Pushover Registration

```
python3 PushoverRegistration.py
```
This will then generate a device.cfg file.

## Push format
The format is as follows:
```
#command On Idx
```
So to turn on a switch that has an id of 14, we would send:
```
#command On 14
```
And to turn it off
```
#command Off 14
```
Other commands available are:
```
#commandToScene On 2
#commandByName Off Main Light
#commandByName On Evening Lighting
```
Note: The #commandByName matches the text with your device and scene names.
To find the Idx go to your Domoticz Url and click on Setup > Devices. This will give you a table of devices that you have set up along with their Idx's. 

## Use with Ifttt
Create an applet with an 'If' of Google assistant, Alexa, or whatever you like.
Set up the 'That' to be pushover.
Using the format mentioned above, push a note with the title e.g. 'Turn on Lamp' and the message as '#command On 14'

## Test that everything works
Run the following command and then send a push via IFTTT e.g. #command On 14
```
python3 /home/pi/scripts/IFTTTtoDomoticzUsingPushover/UsingPushover.py
```

## Adding to startup
First lets create the logs directory.
There are actually many ways to add to startup, the simplest I have found is to add to /etc/rc.local
```
mkdir /home/pi/logs
sudo nano /etc/rc.local
```
Add the following to the bottom (before exit 0)
```
python /home/pi/scripts/IFTTTtoDomoticzUsingPushover/UsingPushover.py  > /home/pi/logs/pushover.log 2>&1
```

reboot - test - done!


This client is not written or supported by Superblock, the creators of Pushover.
