def factorial(num):
    if type(num) is not int or num < 0:
         return None
         
    res = 1
    for n in range(num-1, 1, -1):
        res = num * res
    return res

def factorial_recursive(num):
    if type(num) is not int or num < 0: return None
    
    if num == 0: return 1
    return num * factorial_recursive(num - 1)