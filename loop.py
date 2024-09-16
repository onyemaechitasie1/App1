# i = 1
# while i <= 30:
#     print ("Tasie")
#     i = i + 1


# i = 5
# while i >= 1:
#     print ("Tasie", i)
#     i = i - 1


# i = 5
# j = 1
# while i >= 1:
#     print ("Tasie", i)
#     while j <= 7:
#         print("God'stime, Onyemaechi", j)
#         j = j + 1
#     i = i - 1


# i = 1
# while i <= 4:
#     print ("Tasie ", end="")
#     j = 1
#     while j <= 7:
#         print("God'stime, Onyemaechi ", end="")
#         j = j + 1

#     i = i + 1
#     print()




##User_Prompt with for loop:
# user_prompt = ("Enter a todo: ")


# lst = []

# for i in range(5):
#     todos = input(user_prompt)
#     lst.append(todos)
#     print(lst)
#     print("Enter Next Todo")



#User_Prompt with while loop:
user_prompt = ("Enter a todo: ")

lst = []

i = 1
while i<=5:
    i =i+1
    todos = input(user_prompt)
    lst.append(todos)
    print(lst)
    print("Enter Next Todo")