peoples = {
 'David': {
     'var maskot på uni',
 },
 'Jeff': {
     'født i frankrike'
 },
 'Anna':{
     'Has arachnophobia'
 },
 'Dylan':{
     'Har et pinnsvin'
 }
}
for people in peoples:
    print('{}  {}'.format(people,peoples[people]))
   
print('-------' *5)   
peoples['Jeff'] = 'tissa i buksa'
   
peoples['Potty'] = 'ser bra ut'

for people in peoples:
    print('{}  {}'.format(people,peoples[people]))