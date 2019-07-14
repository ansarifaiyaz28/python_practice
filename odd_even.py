'''
Created on Jul 14, 2019

@author: ansari

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
'''

def odd_even(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
    
number = input("enter number: ")
print("The entered number is ", odd_even(int(number)))
