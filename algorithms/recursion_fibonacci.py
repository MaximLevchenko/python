def fib_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


print(fib_recursive(4))
'''Another example of recursion is below'''
# def factorial(n):
#    print("factorial has been called with n = " + str(n))
#    if n == 1:
#        return 1
#    else:
#        res = n * factorial(n-1)
#        print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
#        return res
#
# print(factorial(5))
