# # Factorial for defined input
# def fact(n):

#     a = 1
#     for i in range(1, n+1):
#         a = a*i

#     return a

# x = 7

# result = fact(x)

# print(result)



# #Not correct! Factorial to take input from the user

# def fact(n):

#     a = 1
#     for i in range(1, n+1):
#         a = a*i

#     return a

# x = "Enter a number: "
# fact = input(x)
# result = fact('x')

# print(result)





# #Recursion
# def greet():
#     print('Hello')
#     greet()

# greet()



#Recursion above 1000 limit
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

p = 0
def greet():
    global p
    p+=1
    print('Hello', p)
    greet()

greet()