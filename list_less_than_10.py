'''
Created on Jul 14, 2019

@author: ansari

Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 10.
'''
def list_less_than_ten(num_list):
    return [x for x in num_list if x<10]
    
'''
#input list by space separated
a = input("enter list of numbers separated by a single space ")
a = list(map(int,a.split(' ')))

'''

'''
#input list by comma separated
a = input("enter list of numbers separated by a single comma ")
a = list(map(int,a.split(',')))
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print(a,"\nThe numbers less than 10 from above list are:\n", list_less_than_ten(a))

#to print only non repeated numbers
#print(a,"\nThe numbers less than 10 from above list are:\n", list(set(list_less_than_ten(a))))

