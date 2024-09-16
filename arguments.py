# def sum(a,b): #a and b here are referred to as "formal argument"
#     c = a+b
#     print(c)

# sum(9,7) #9 and 7 here are referred to as "actual argument"



##Position argument
# def person(name, age):
#     print("My name is", name)
#     print("I am",age, "years old")

# person("Tasie", 20)




# #Keyword argument
# def person(name, age):
#     print("My name is", name)
#     print("I am",age, "years old")

# person(age=20, name="Tasie")





# #Default argument
# def person(name, age=18):
#     print("My name is", name)
#     print("I am",age, "years old")

# person(name="Tasie")





##Variable argument
# def greet(a, *b): # *b is used when the variable contains more than one variable(tuple)
    
#     c = a
#     for i in b:
#         c = c + i
#     print(c)

# greet(5, 7, 85, 60,20) # a=5, b=7,85,60,20 (tuple)




# def sum(*b):
#     c=0 #c=0 since there is no 'a' variable
#     for i in b:
#         c=c+i
#     print(c)

# sum(5, 6, 7, 9)




# def person(name, address):
#     print("Your name is:", name)
#     print("Your address is:", address)

# person("Ugochukwu Kanu", "#15 Elipolu Rd, Rukpokwu")




# def person(name, **data): # ** means you are passing multiple arguement(tuple) keyword
#     print("Name :", name)


#     for i,j in data.items():
#         print(i,j)

# person("Tasie", Age=": 20", Address=": Port Harcourt", Phone=": 8244958",)





# def greet(a,b):
#     c=a+b
#     return c

# result = greet(5.7, 6.9)
# print(result)
