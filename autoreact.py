import pyperclip
from win10toast import ToastNotifier
from pyautogui import press, typewrite, hotkey, keyDown, keyUp

string_to_search = 'The first person to type' #Variables
list_of_results = []
line_number = 0
toaster = ToastNotifier()

             

def read_file():
    with open("C:\\Users\\austi\\AppData\\Local\\.ftba\\instances\\f91780f7-7749-4feb-a8fa-2affba007e53\\logs\\latest.log", "r") as f:
        SMRF1 = f.readlines()
    return SMRF1    #Looping function/Keep Alive

initial = read_file()
while True: #Looping Function that loops code
    current = read_file()
    if initial != current:
        for line in current:
            if line not in initial:
                print(line)
        initial = current
        with open("C:\\Users\\austi\\AppData\\Local\\.ftba\\instances\\f91780f7-7749-4feb-a8fa-2affba007e53\\logs\\latest.log", 'r') as read_obj: #Defines where to open the file from
            for line in read_obj:
                line_number += 1
                if string_to_search in line:
                    list_of_results.append((line_number, line.rstrip()))
                    potato = (line.split(' '))    #Potato is the array to index from
                    print(potato[10])
                    pyperclip.copy(potato[10])
                    #press('t')
                    #keyDown('ctrl') #Paste the word into chat
                    #press('v')
                    #keyUp('ctrl')

                    with open("C:\\Users\\austi\\AppData\\Local\\.ftba\\instances\\f91780f7-7749-4feb-a8fa-2affba007e53\\logs\\latest.log", "r") as f:
                        lines = f.readlines()
                    with open("C:\\Users\\austi\\AppData\\Local\\.ftba\\instances\\f91780f7-7749-4feb-a8fa-2affba007e53\\logs\\latest.log", "r+") as f:
                        for line in lines:
                            if line.strip("\n") != "The first person to type":
                                f.write(line)

                    #toaster.show_toast("Word Detected!",potato[10]) #Makes A win notification upon word discovery
                    x = len(potato) #Checks length of array if it is over 15 it detects that it is a multi word and proceeds
                    if x == 15: #For multiword reactions
                        print(' '.join(potato[10:12]))
                        pyperclip.copy(' '.join(potato[10:12]))
                        press('t')#Opens Chat
                        press(['ctrl', 'v']) #Paste the word into chat
                    if x == 16:
                        print(' '.join(potato[10:13]))
                        pyperclip.copy(' '.join(potato[10:13]))
                        press('t') #Opens Chat
                        press(['ctrl', 'v']) #Paste the word into chat







