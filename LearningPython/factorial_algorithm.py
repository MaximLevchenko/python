def factorial(value):
    if value==1:
        return 1
    else:
        val=value**factorial(value-1)
factorial(5)
