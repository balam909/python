# Creating a single list
print("Creating a simple list")
a=["a","b","c","d","e"]
print("You use this line of code to create a list: 'a=[\"a\",\"b\",\"c\",\"d\",\"e\"]'")
print("This is the result: ",a)
print("If you need a serie number list, this is a better option: range(n), where 'n' is a number")
b=range(10)
c=[]
for x in b:
	c.append(x) # append, add a the end of a list one element
print("This is your list: ",c)
# If you need to iterate a list arround the indexes
print("Now we will iterate the list using the list indexes: ")
for i in range(len(a)):
	print(i,"-",a[i])

# Appending lists
print("Append lists")
a=["a","b","c","d","e"]
print("a=",a)
b=["f","g","h","i","j"]
print("b=",b)
a.extend(b)
print("La lista resultante es: ",a)

# Lists as stack or queues
pila=[1,2,3,4,5,6,7,8,9]
print("pila=",pila)
print("Use append to add a new alement at the end of the list, using pila.append(0)")
pila.append(0)
print("This is the new value for pila: ",pila)
print("Now using pila.pop(), we can take from the list the last added element")
pila.pop()
print("This is the new value for pila: ",pila)
print("Now we will pop 3 times: ")
pila.pop()
pila.pop()
pila.pop()
print("This is the new value",pila)
print("Now we will add one more element")
pila.append(9)
print("The current value for pila is: ",pila)
print("To remove the first element added into a list, we can use pop(0), for the stack: ",pila,"lets remove the first two elements")
pila.pop(0)
pila.pop(0)
print("Now this is our list",pila)
