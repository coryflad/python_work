# Accessing items within a List

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# returns first element in the bicycles list and capitalize it
print(bicycles[0].title())

# return the last element in the bicycles list
print(bicycles[-1].title())

# return the second to the last element in the bicycles list
print(bicycles[-2].title())

# use and indvidual element from the list 
message = f"My first road bike was a {bicycles[0].title()}!"
print(message)