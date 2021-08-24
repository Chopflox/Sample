groceryList = []
maxItems = 3

while len(groceryList) < maxItems:
    item = input('watchu wanna buy? ')
    groceryList.append(item)
    print(groceryList)

print('--------------------------------')
print(groceryList) 
