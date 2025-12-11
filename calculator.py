food = ['rice', 'garri', 'egg', 'pork']
print(food[0])

food[0] = 'yam'
print(food)

# adding an iterm
food.insert(0, 'beans')
food.insert(3, 'plum')
food.append('eru')

print(food)

# removing an item
food.remove('pork')
food.pop(2)
print(food)

# sorting
food.sort()
print(food)
food.sort(reverse=True)
print(food)
