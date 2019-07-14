'''
Created on Jul 14, 2019

@author: ansari

Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''
def age_func(age):
    import datetime
    return datetime.datetime.now().year + (100-age) #get present year + years to reach 100 year old
    
      
name = input("Name: ") #gives str data types
age = input("Age: ") #gives str data types
#so we need to change age to integer type
print("In ",age_func(int(age)),", " + name + " will turn 100 years old.")

