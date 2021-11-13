import json
from os import system
from os.path import exists
from time import sleep


print("██╗░░░██╗███╗░░░███╗░█████╗░███╗░░██╗░██████╗░██╗░░██╗")
print("██║░░░██║████╗░████║██╔══██╗████╗░██║██╔════╝░╚██╗██╔╝")
print("██║░░░██║██╔████╔██║███████║██╔██╗██║██║░░██╗░░╚███╔╝░")
print("██║░░░██║██║╚██╔╝██║██╔══██║██║╚████║██║░░╚██╗░██╔██╗░")
print("╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║╚██████╔╝██╔╝╚██╗")
print("░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝")




def connection(add):
    print("------------------------------------")
    system("bluetoothctl disconnect " + add)
    print("------------------------------------")
    sleep(2)
    print("------------------------------------")
    system("bluetoothctl connect " + add)
    print("------------------------------------")


def entry():
    print("Enter the mac address:")
    heads = {"address": "Unknown", "name": "Heads"}
    heads["address"] = input()
    print("Enter name of the device:")
    heads["name"] = input()
    with open("~/umangx/config.json", 'w') as file_object:
         json.dump(heads, file_object)


def file_check():
    if exists("~/umangx/config.json") == True:
        with open("~/umangx/config.json") as file_object:
            data = json.load(file_object)
        if data["address"] != 0:
            connection(data["address"])
        else:
            empty()
    else:
        empty()


def empty():
    system("touch ~/umangx/config.json")
    entry()
    # with open('config.json','w') as file_object:
    #     json.dump(heads,file_object)
    file_check()


file_check()
