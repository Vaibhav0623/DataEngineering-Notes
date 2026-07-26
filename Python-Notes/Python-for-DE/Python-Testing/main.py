
def get_weather(temp):
    if temp > 20:
        return 'Hot'
    else:
        return 'Cold'

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError ("Cannot divide by zero") 
    return a / b

