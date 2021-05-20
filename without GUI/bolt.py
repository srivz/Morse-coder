import time
from boltiot import Bolt

api_key = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" #API_KEY for the bolt_device 
device_id = "BOLTxxxxxxxx" #BOLT DEVICE_ID


mybolt = Bolt(api_key, device_id)

def tomorse(text):
    a = text.lower()
    morse_dict = {"a": ".- ", "b": "-... ", "c": "-.-. ", "d": "-.. ", "e": ". ", "f": "..-. ", "g": "--. ", "h": ".... ", "i": ".. ", "j": ".--- ", "k": "-.- ", "l": ".-.. ", "m": "-- ", "n": "-. ", "o": "--- ", "p": ".--. ", "q": "--.- ", "r": ".-. ", "s": "... ", "t": "- ", "u": "..- ", "v": "...- ", "w": ".-- ", "x": "-..- ", "y": "-.-- ", "z": "--.. ", " ": "/ ", ",": "--..-- ",  ".": ".-.-.- ", "/": "-..-. ", ":": "---... ", "!": "-.-.-- ", "@": ".--.-. ", "1": ".---- ", "2": "..--- ", "3": "...-- ", "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ", "8": "---.. ", "9": "----. ", "0": "----- ", "&": ".-... ", "(": "-.--. ", ")": "-.--.- ", "+": ".-.-. ", "=": "-...- ", "?": "..--.. ", "-": "-....- ", "\n": "\n", "\t": "\t"}
    final = ""
    for i in a:
        final = final + morse_dict[i]
    return final

def send(co):
        code = tomorse(co)
        print(code)
        time.sleep(3)
        response = 0
        for j in code:
            time.sleep(0.03)
            if j == ' ':
                time.sleep(0.2)
            elif j == '/':
                time.sleep(1)
            else:
                if j == '-':
                    mybolt.digitalWrite('0', 'HIGH')
                    time.sleep(0.3)
                    response = mybolt.digitalWrite('0', 'LOW')

                elif j == '.':
                    mybolt.analogWrite('0', 240)
                    time.sleep(0.001)
                    response = mybolt.digitalWrite('0', 'LOW')
        print("Message transmission is " + str(response))
        if response[-2] == 0:
            exit()
n=input("Enter your message: ")
send(n)

