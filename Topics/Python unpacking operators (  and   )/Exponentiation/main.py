info = input().split(', ')
name, age, city, *miscellaneous = info

print('name:', name)
print('age:', age)
print('city:', city)
print('miscellaneous:', *miscellaneous)
