# my_lambdata/ds_utilities.py

def enlarge(n):
    '''This function will multiple the input by 100'''
    return n * 100

y = int(input("Choose a number: "))
print(y, enlarge(y))