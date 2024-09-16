# a = 20 #Global variable
# def free():
#     a = 10 #Local variable
#     print("local variable", a)

# free()
# print("global variable", a)






# #You can use global variable as local variable
# a = 10

# def sudden():

#     print("inside function", a)

# sudden()
# print("outside function", a)





# #You can use local variable as global variable by using the keyword "global a"
# a = 10

# def sudden():

#     global a
#     a = 70
#     print("inside function", a)

# sudden()
# print("outside function", a)






# # Using globals keyword
# a = 10
# print(id(a))

# def deep():
#     a = 9
#     x = globals()['a']
#     print(id(x))
#     print("inside func", a)

# deep()

# print("outside func", a)




def count(list):
    even = 0
    odd = 0

    for i in list:
        if i%2==0:
            even+=1
        else:
            odd+=1

    return even,odd

list = [23, 44, 67, 87, 62, 89, 43, 90]
even,odd = count(list)
print("even", even)
print("odd", odd)






# # Global and local variable test
# (x,y) = (6,12)
# a = x + y
# def deen(x,y):
#     b = x * 2 * y
#     return b

# b = deen(9, 4)
# print("Inside value is;", b)
# print("outside value is:", a)