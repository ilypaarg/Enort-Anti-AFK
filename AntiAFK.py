import time
import colorama
from colorama import Fore, Style
import random
import os
import keyboard
import pynput
import pynput.keyboard
from pynput.keyboard import Key, Controller
import array

# Setting up random times

interval = [0.01] # Interval can be edited.

presses = ['w', 'a', 's', 'd', 'w', 'a', 's', 'd', 'w', 'a', 's', 'd', Key.space, Key.space, Key.space, Key.shift, Key.shift, Key.shift]

timer = (random.choice(interval))
rpress = (random.choice(presses))

# Declaration of key presses in order for it to recognize later.

keyboard = Controller()

def type_string_with_delay(string):
  for character in string:
    keyboard.press(character)
    delay = random.uniform(1, 30)
    time.sleep(delay)
    
 os.system('cls')
print(Fore.LIGHTCYAN_EX + "Enort ANTI AFK | By: Enortis The Great | v1.0")
time.sleep(3)
os.system('cls')
time.sleep(3)
print(Fore.LIGHTCYAN_EX + "In order for this to work, please leave the console window open while you are afk.")
time.sleep(5)
os.system('cls')

print(Fore.LIGHTCYAN_EX + "Press any key to start the Anti AFK.")
os.system('pause')
print(Fore.LIGHTCYAN_EX + "Starting")
print(Fore.LIGHTRED_EX + "5")
time.sleep(1)
print(Fore.LIGHTRED_EX + "4")
time.sleep(1)
print(Fore.LIGHTRED_EX + "3")
time.sleep(1)
print(Fore.LIGHTRED_EX + "2")
time.sleep(1)
print(Fore.LIGHTRED_EX + "1")
time.sleep(1)
os.system('cls')
print(Fore.LIGHTCYAN_EX + """
 _____    _    _   _   _   _   _   _____   _   _    _____ 
|  __ \  | |  | | | \ | | | \ | | |_   _| | \ | |  / ____|
| |__) | | |  | | |  \| | |  \| |   | |   |  \| | | |  __ 
|  _  /  | |  | | | . ` | | . ` |   | |   | . ` | | | |_ |
| | \ \  | |__| | | |\  | | |\  |  _| |_  | |\  | | |__| |
|_|  \_\  \____/  |_| \_| |_| \_| |_____| |_| \_|  \_____|
                                                          
                                                             
""")
time.sleep(1)
for balls in range(1000000000000000000000000000000000):
    keyboard.press(random.choice(presses))
    time.sleep(0.01)
    keyboard.release('w')
    time.sleep(0.01)
    keyboard.release('a')
    time.sleep(0.01)
    keyboard.release('s')
    time.sleep(0.01)
    keyboard.release('d')
    time.sleep(0.01)
    keyboard.release(Key.space)
    keyboard.press(Key.shift)
    time.sleep(0.01)
    keyboard.release(Key.shift)
    time.sleep(0.01)
    time.sleep(random.choice(interval))
    time.sleep(0.01)

time.sleep(0.01)
