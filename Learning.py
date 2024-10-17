"""print("Welcome to the world of python.")
n1 = "86"
n2 = "87"
print(100 * str(int(n1) + int(n2)))"""
"""
print("Enter your 1st Number")
n1 = input()
print("Enter your 2nd Number")
n2 = input()
print("The Sum of your numbers is", int(n1) + int(n2))

x = "The world is a beautiful place"
print(len(x))
print(x[:-5:-2])
'''
'''grocery = ["Harpic", "Vim bar", "Deodrant"]
print(grocery[0])'''
'''numbers = [1, 2, 3, 4, 5, 8, 7, 6]
numbers.append(9) #append adds the given value to the end of list
numbers.insert(2, 10) #inserts an object to a specified index
numbers.sort() #Sort sorts the list in increasing order
numbers.remove(8) #Removes an object from the list
numbers[1] = 10 #Changes the number from the specified index of list
print(numbers[0:10:1])'''

# Mutable - can change
# Immutable - cannot change

"""
"""d1 = (1,)#Tuple
print(type(d1))"""
"""a = 5
b = 6
print(a,b)
a = b
print(a,b)"""

'''dictionary = {}
print(type(dictionary))'''

"""d2 = {"Harry":"Burger", "Rohan":"Fish", 
      "Tanishk": {"Morning": "Raita", "Dinner": "Chicken"}}
#print(d2["Tanishk"])
d2["Pita shri"] = "Dahi Bhalle" #for adding something in dictionary
del d2["Rohan"] #for deleting someting from a dictionary
print(d2)"""

"""list1 = [ ["Harry", 1], ["Larry", 2], ["Carry", 3]]
dict1 = dict(list1)
for item in dict1:
      print(item)"""

"""items = [int, float, "Herry", 5, 6, 7, 3, 2]
for item in items:
      if str(item).isnumeric() and item>=6:
            print(item)"""

"""a = 0
while(True):
      if a<5:
            a = a+1
            continue
      if a<50:
            print(a, end=" ")
      if a==50:
            break
      a = a+1"""

"""while(True):
      inp = int(input("Enter any Number: "))
      if inp>100:
            print("Congratulations, You have entered a number greater than 100")
            break
      else:
            print("Try again!")
            continue"""

