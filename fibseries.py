# def fib(n):
#     print(0)
#     print(1)

# fib(5)





# def fib(n):
#     a = 0
#     b = 1

#     print(a)
#     print(b)

#     for i in range (2, n):
#         c = a+b
#         a = b
#         b = c
#         print(c)

# fib(5)



#Fib series for n=1
def fib(n):
    a = 0
    b = 1

    if n == 1:
        print(a)        
    else:
        print(a)
        print(b)

        for i in range (2,n):
            c = a+b
            a = b
            b = c
            print(c)


fib(1)



# #Fib series for n>0 but less than 50
# def fib(n):
#     a = 0
#     b = 1

#     if n<0:        
#         print ('n is not valid')
#     elif n>50:
#         print('n is way too big, cannot print')
#     else:
#         print(a)
#         print(b)

#         for i in range (2,n):
#             c = a+b
#             a = b
#             b = c
#             print(c)


# fib(32)