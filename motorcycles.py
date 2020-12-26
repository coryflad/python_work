motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

# modify an element in a list
# motorcycles[2] = 'ducati'
# print(motorcycles)

# add elements to a list
# motorcycles.append('harley-davidson')
# print(motorcycles)

# insert element into list and specifying the index of the new element
# motorcycles.insert(0, 'ducati')
# print(motorcycles)

# removing an element
# del motorcycles[0]
# print(motorcycles)

# using .pop method
# last_owned = motorcycles.pop(2)
# print(f"The last motorcycle I owned was a {last_owned.title()}.")

# remove an item by value, used when you don't know the order of the position
# motorcycles.remove('ducati')
# print(motorcycles)

# work with value that is being removed
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")



