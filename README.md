# Morse-coder
The international Morse code distress signal was first used by the German government in 1905 and became the standard distress signal around the world just a few years later. It is even used by the military spies to smuggle information from enemy countries. And moreover, it is fun !!!!!

Hardware connections:

*Connect the positive(or longer pin or red wire) and the negative(or short pin or black wire) of both LED and buzzer to the 0th port and to the GND port of the Bolt WiFi module respectively.

*Attach a resistor to the LED for reducing the voltage that is being passed through the circuit. (This is not mandatory. This is done for precaution so that the LED won't fuse.)

*Connect USB (Type C) wire to the Bolt WiFi module and provide a power supply.(Note: Once your Bolt WiFi module gets power supply then the blue LED in it will start blinking and become stable. And once your module is connected to the registered WiFi the green LED will be on.)


Software prerequisites:

Firstly you must make sure you have to set up the following correctly:

1) First, create an account in the bolt cloud. You can do so in the below link:

https://cloud.boltiot.com/login

2) Create an account in Twilio.

3) Create an account in Mailgun.

4) Install Bolt Python Library.

In the terminal type the below codes separately:

=> sudo apt-get y update

=> sudo apt install python3-pip

=> sudo pip3 install boltiot


5) Install kivy package by the following command:

sudo apt-get install python-kivy

FURTHER INSTRUCTIONS:

In case you are struggling to find your Device ID or API key.

You can see your Device ID in https://cloud.boltiot.com/home/ and your API key in https://cloud.boltiot.com/api_credentials.

For sending long messages:

You can update your account to pro pack for transmitting long messages. You can view your plan through this link: https://cloud.boltiot.com/view_profile/plan
