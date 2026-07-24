# This code Showing How To Handle The Error

try:
    f = open('currupt_file.txt')

# This is the Mannul Raise Exception

"""
    if f.name == 'currupt_file.txt':
        raise Exception
"""    

except FileNotFoundError as e:
    print(e)

except Exception as e:
    print('Error!')

else:
    print(f.read())
    f.close()

finally:
    print("Executing Finally...")





