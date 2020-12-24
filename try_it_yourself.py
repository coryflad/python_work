# These are the "Try It Yourself" problems from Python Crash Course

# 2-1
# message_1 = "This is the first problem I solved!"
# print(message_1)

# 2-2
# message_2 = "I am going to change message_2..."
# print(message_2)

# message_2 = "to print to be message_3?"
# print(message_2)

# 2-3
# name = "Cory"
# personal_message = f"Hello {name.title()}, would you like to learn some Python today?"
# print(personal_message)

# 2-4
# name_case = "gary cannalte"
# print(name_case)
# print(name_case.title())
# print(name_case.upper())

# 2-5 / 2-6
# famous_author = "albert einstein"
# famous_quote = "A person who never made a mistake never tried anything new!"
# sentence = f"{famous_author.title()} once said, \"{famous_quote}\""
# print(sentence)

# 2-7
# text = "    The woods are lovely, dark and deep,    \n"
# remove new line and all space
# print(text.strip())

# remove only spaces
# print(text.strip(" "))

# remove everything to the left
# print(text.lstrip())

# remove everything to the right
# print(text.rstrip())

# remove "d" character either end of the string
# message1 = "decided"
# print(message1.strip('d'))

# remove specfic characters from a string
# message2 = ",.,...!?!?.Nice...:"
# sanitized_message = message2.strip(".,!?:()")
# print(sanitized_message)

# 2-8
# addition = 4+4
# subtraction = 16-8
# multiply = 4*2
# divide = 16/2

# print(addition)
# print(subtraction)
# print(multiply)
# print(divide)

# 2-9
# favorite_num = 3*9
# num_name = "Cory"
# num_sentence = f"{num_name}'s favorite number is {favorite_num}!"
# print(num_sentence)

# 3-1
# names = ['mom', 'becky', 'stanley the dog', 'gary']
# print(names[2].title())

#3-2
# simple_message = f"Hello there {names[2].title()}. How are you doing today?"
# print(simple_message)

# 3-3
# time_of_day = ['morning', 'afternoon', 'evening']
# detailed_message = f"Hello {names[2].title()}. How are you doing this {time_of_day[1]}?"
# print(detailed_message)