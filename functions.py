def greet(): #def is definition of function
    message = ("Hello")
    return message
jp = greet()
print(jp)

# greet() #greet here means you are calling the funtion

# greet () #You can call your function multiple times




# #Addition of variable in a function
# def greet():
#     print("Hello")
#     print("Good morning")


# def add(x, y): # x, y here means you are passing an argument
#     c = x + y
#     return c

# ben = add(5,4)
# print(ben)



# def add(x, y): # x, y here means you are passing an argument
#     c = x + y
#     print(c)

# greet()
# add(5,4)



# #Function with return
# def add(x, y):
#     c = x + y
#     return c #return is a keyword which is used to return a value

# result = add(5,4)
# print(result)



#Function with add and sub
# def add-sub(x, y): 
#     c = x + y
#     d = x - y
#     return c,d

# result1, result2 = add_sub(5,4)
# print(result1)
# print(result2)





# #Function Argument
# def update(x): #update function will take a value from a user
#     x = 8
#     print(x)

# update(10)



# def update(x): #update function will take a value from a user
#     x = 8
#     print("Xender", x)

# a = 10
# update(a)
# print("Alex", a)




# #Printing ids of variable function
# def update(x):
#     print(id(x))
#     x = 8
#     print(id(x))
#     print("x", x)

# a = 10
# print(id(a))
# update(a) 
# print("a", a)




# #Printing immutable function
# def update(list2):
#     list2 = {5, 10, 15, 20, 25}
#     x = sum(list2)
#     print("The sum in list2 is:", x)
#     print("list2", list2)

# list1 = {10, 20, 30}
# y = sum(list1)
# print("The sum in list1 is:", y)
# update(list1) 
# print("list1", list1)




# #Printing immutable function
# def update(list2):
#     list2 = {5, 10, 15, 20, 25}
#     x = sum(list2)
#     print("The sum in list2 is:", x)

# list1 = {10, 20, 30}
# y = sum(list1)
# print("The sum in list1 is:", y)
# update(list1) 




# #Average Marks using print function
# def update():
#     marks = {55, 64, 75, 80, 65}
#     length = len(marks)
#     sum_of_marks = sum(marks)
#     average_marks = sum_of_marks / length
#     print("Your average mark is:", average_marks)

# update()





# #Average marks using return function
# def update(marks):
#     Lenth = len(marks)
#     Summation_of_marks = sum(marks)
#     average_marks = Summation_of_marks/Lenth
#     return average_marks
    
# marks = {55, 64, 75, 80, 65}
# average_marks = update(marks)
# print("The average mark is:", average_marks)





# # Calcuting average marks and getting your grade for an examination
# def update(marks):
#     Length = len(marks)
#     Summation_of_marks = sum(marks)
#     average_marks = Summation_of_marks/Length
#     return average_marks
    

# def grade(average_marks):
#     if average_marks >= 80:
#         grade = 'A'
#     elif average_marks >= 60:
#         grade = 'B'
#     elif average_marks >= 50:
#         grade = 'C'
#     else:
#         grade = 'F'
#     return grade


# marks = {55, 64, 75, 80, 65}
# average_marks = update(marks)
# print("The average mark is:", average_marks)

# grade = grade(average_marks)
# print ("Your grade is:", grade)






# # Taking input from a user on getting grade of an examination
# score = int(input("Enter Your Score: "))

# if score > 100 or score < 0:
#     print ("Sorry, your score is not valid")

# elif score >= 80:
#     print("Your grade is A")

# elif score >= 60:
#     print("Your grade is B")

# elif score >= 50:
#     print("Your grade is C")

# else:
#     print("Sorry, you failed your exam")






# #Taking input from a user to check if a number is positive or negative
# number = float(input("Input Your Number: "))

# if number < 0:
#     print("The number is negative")

# elif number > 0:
#     print("Your number is postitive")

# else:
#     print("The number is 0")
