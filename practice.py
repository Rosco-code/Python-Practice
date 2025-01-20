'''
Okay, so according to ChatGPT, if I wanted to master Python, there would be 7 steps. Which are listed below.
Step 1: Master Python Basics
Step 2: Build Small Projects
Step 3: Explore Python Libraries
Step 4: Learn A Framework
Step 5: Work On Bigger Projects
Step 6: Learn Best Practices
Step 7: Expirement With New Technologies

So let's begin.
'''

#1/16/2025  8:36AM PST
#According to line 3. Step 1 in the process is Mastering Python Basics, which makes sense to me. So what is the first basic that i want to focus on? Or maybe the question is what are the basics? According to chatgpt Syntax and Basic Constructs are #1 so that's where I'll start. Just not right now because I want to smoke a ciggarette and watch TV.

#1/16/2025 9:28AM PST
some_names = a, b, c, d, e = "Tommy", "Alice", "Bobby", "Chidi", "Ricardo"
some_variables = a, b, c, d, e, f, g = 1, 2, 3, 4, 5, 6, 7
best_sushi = {"name": "Shiro's", "location": (47.61477069277289, -122.34742595599339), "origin": "Japan", "price": "High", "quality": "High"}
# # print(someVariables[3])
# # b = a/a
# # print(b)

# for x in some_variables:
#     # print(x**x)


#     def global_keyword():
#         global c
#         c = 1
#         print(c)
#     global_keyword()

# for x in some_names:
#     # print(x[0].lower())

# # print(some_names[1], some_variables[1])

#     for x in best_sushi:
#         sushimi = x
#     # print(sushimi)

# # print(best_sushi["name"])

#1/17/2025 7:41AM PST
# user = input('I am python. What is your name? : ')
# print('Welcome' , user)

# print("Hello,", "Tommy", sep = '... ', end = '!\')

# a = (1 + 1) % 3
# print(a)

# a = True
# b = False2

# print('AND logic:')
# print('a and a = ', a and a)
# print('a and b = ', a and b)
# print('b and b = ', b and b)
# print('1 and 1 = ', 1 and 1)
# print('1 and 0 = ', 1 and 0)
# print('0 and 0 = ', 0 and 0)

# print('OR logic:')
# print('a or a = ', a or a)
# print('a or b = ', a or b)
# print('b or b = ', b or b)

# print('NOT logic:')
# print('a =', a, ' not a = ', not a)
# print('b =', b, ' not b = ', not b)

#1/18/2025 6:33AM PST
# a = input('Enter A Number: ')
# b = input('Now Enter Another Number: ')

# sum = int(a) + int(b)
# print('Data Type sum: ', sum, type(sum))
# sum2 = int(a) + int(b)
# print('sum2 is a: ', type(sum2), ', The value of sum2 is: ', sum2)
# sum = chr(int(sum))
# print('Data type sum: ', sum, type(sum))

#this XOR bit algorithim requires three steps and then swaps the values of the two variables. the variables have to be ints, they cant be floats, str or anything else.
# a = 20.5
# b = 10.5
# print('a = ', a, 'b = ', b )

# a = a ^ b
# b = a ^ b
# a = a ^ b
# print('a = ', a, 'b = ', b )

# quarter = ['January', 'February', 'March']

# print('First month: ', quarter[0])
# print('Second month: ', quarter[1])
# print('Third month: ', quarter[2])

# coords = [[1, 2, 3], [4, 5, 6]]
# print('Top Left 0, 0 :', coords[0][0])
# print('Bottom Right 1, 2', coords[1][2])
# print("Second Month's first letter: ", quarter[1][0])

#1/19/2025 4:58PM PST
# basket = ['Apple,', 'Bun', 'Cola']
# crate = ['Egg', 'Fig', 'Grape']

# print('Basket List: ', basket)
# print('Length of Basket List: ', len(basket))

# basket.append('Damson')
# print('Appended: ', basket)
# print('Last Item Removed: ', basket.pop())
# print('Updated Basket: ', basket)

# basket.extend(crate)
# print('Extended Basket List: ', basket)
# del basket[1]
# print('Item removed from basket index position 1: ', basket)
# del basket[1:3]
# print('Slice Removed basket index of [1:3]', basket)

# zoo = ('Kangaroo', 'Leopard', 'Moose')
# bag = {'Red', 'Green', 'Blue'}
# box = {'Red', 'Purple', 'Yellow'}
# print('Tuple: ', zoo, 'Length: ', len(zoo))
# print(type(zoo))
# bag.add('Yellow')
# print('Set: ', bag, 'Length: ', len(bag))
# print(type(bag))
# print('Is green in bag set? ', 'Green' in bag)
# print('Is Organge in bag set? ', 'Orange' in bag)
# print('Set: ', box, 'Length: ', len(box))
# print('Common items from box and bag sets: ', bag.intersection(box))

userSys = {'name' : 'Bob', 'sys' : 'Win'}
userLang = {'name' : 'Bob', 'lang' : 'Python'}
dict = userSys | userLang
print('Dictionary: ', dict)
# | is no longer the merge operator for dictionaries. which is why the code above and in the book fails. I will look up how to merge two dictionaries later. based on what i saw in chatgpt/google. now you copy one dictionary into a third dictionary then append the second dictionary into that third dictionary.



