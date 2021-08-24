import random
from typing import KeysView
peopleF = {
 'David': {
 'Fun fact': 'var maskot på uni',
 'Another fun fact': 'kan trikse'    
 },
 'Jeff': {
 'Fun fact': 'født i frankrike'
 },
 'Anna': {
 'Fun fact': 'Has arachnophobia'
 },
 'Dylan': {
 'Fun fact': 'Har et pinnsvin'
 }
}

names = 'david', 'Jeff', 'Anna', 'Dylan'

peopleFR = random.choice(list(peopleF.values()))
peopleRV = random.choice(names)


print(names)
print(peopleFR)